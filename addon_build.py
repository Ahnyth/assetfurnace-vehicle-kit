"""AssetFurnace add-on entry: build one vehicle with the shape-guide kit and leave `{out}/{stem}.glb`.

Runs inside Blender (the add-on's `run` starts `{blender}` with this file), so it needs no
Python of its own on the user's machine. It starts the vehicle family's builder as a second
headless Blender, exactly as `shape_guide.py` does from the command line, and then copies the
result AssetFurnace looks for: `<stem>_parts.glb` (body, wheels and doors as parts on their
pivots) or, with "One mesh", `<stem>_joined.glb`, as `<stem>.glb`, where the stem is the name of
the run folder AssetFurnace made. The atlas and the other file stay beside it.

    blender -b --factory-startup -P addon_build.py -- OUT_DIR PRESET ATLAS [JOINED]
"""

import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import shape_guide  # plain maths, no bpy

YES = {"1", "true", "yes", "on"}


def plan(argv: list[str]) -> tuple[Path, str, int, bool]:
    """(out_dir, preset, atlas, joined) from the arguments after Blender's `--`."""
    args = argv[argv.index("--") + 1:] if "--" in argv else argv
    if len(args) < 3:
        raise SystemExit("usage: addon_build.py -- OUT_DIR PRESET ATLAS [JOINED]")
    out_dir, preset, atlas = Path(args[0]), args[1], int(args[2])
    if preset not in shape_guide.PRESETS:
        raise SystemExit(f"unknown vehicle {preset!r}; one of {', '.join(shape_guide.PRESETS)}")
    joined = len(args) > 3 and args[3].strip().lower() in YES
    return out_dir, preset, atlas, joined


def main(argv: list[str]) -> int:
    out_dir, preset, atlas, joined = plan(argv)
    import bpy  # only inside Blender: the path of the Blender that runs this file

    stem = out_dir.name
    out_dir.mkdir(parents=True, exist_ok=True)
    command = shape_guide.blender_command(Path(bpy.app.binary_path), preset, out_dir.resolve(), stem, atlas)
    done = subprocess.run(command, check=False)
    if done.returncode:
        return done.returncode
    made = out_dir / f"{stem}_{'joined' if joined else 'parts'}.glb"
    if not made.is_file():
        print(f"vehicle-kit: the builder wrote no {made.name}", file=sys.stderr)
        return 1
    shutil.copyfile(made, out_dir / f"{stem}.glb")
    print(f"vehicle-kit: {preset} -> {stem}.glb")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
