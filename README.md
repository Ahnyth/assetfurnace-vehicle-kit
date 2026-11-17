# Vehicle kit (AssetFurnace add-on)

A detailed bus, metro car or van from a few numbers, no picture needed: the kit lays out the windows, doors,
wheels and lights by rule, builds body, wheels and doors as parts on their pivots, and paints one atlas.

![A box van and a metro car made with the kit](https://raw.githubusercontent.com/AssetFurnace/assetfurnace-addons/main/pictures/vehicle-kit.jpg)

Presets: `bus_12m`, `bus_12m_rule`, `midibus_9m`, `metro_car` (one Blender builder) and `ambulance`, `van_long`,
`box_van` (the other). The result is the parts file (`<run>.glb`): body, wheels and doors as separate parts on their
pivots, so a game can turn the wheels and open the doors. "One mesh" gives the joined version instead. The atlas
(1024, 2048 or 4096 px) and the other file stay in the run folder.

## What it does on your machine

- Runs entirely on your machine; no network, nothing downloaded, no models used.
- Starts Blender (4.2 or newer) as AssetFurnace's add-on runner asks, and from it one more headless Blender for the
  vehicle family's builder; no other programs.
- Writes only into the run folder AssetFurnace gives it.

## Use

In the studio: Add-ons, Vehicle kit, Build a vehicle. From the command line:

    ./lab addon add --unlisted https://github.com/Ahnyth/assetfurnace-vehicle-kit@<commit>
    ./lab addon run vehicle-kit build --preset midibus_9m --atlas 2048 --mesh parts

The layout maths is tested without Blender: `python -m pytest tests`.

It grew out of [image-to-3dlab#261](https://github.com/Bingeljell/image-to-3dlab/pull/261), the shape-guide kit,
which is an add-on now instead of a core change.

Licence: Apache-2.0.
