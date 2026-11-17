# Vehicle kit (AssetFurnace add-on)

A detailed bus, metro car or van from a few numbers, no picture needed: the kit lays out the windows, doors,
wheels and lights by rule, builds body, wheels and doors as parts on their pivots, and paints one atlas.

Presets: `bus_12m`, `bus_12m_rule`, `midibus_9m`, `metro_car` (one Blender builder) and `ambulance`, `van_long`,
`box_van` (the other). The result is the parts file (`<run>.glb`); "One mesh" gives the joined version instead. The
atlas and the other file stay in the run folder.

Needs Blender 4.2 or newer; it runs entirely on your machine and downloads nothing.

    ./lab addon add --unlisted <this repo>@<commit>
    ./lab addon run vehicle-kit build --preset midibus_9m --atlas 2048

The layout maths is tested without Blender: `python -m pytest tests`.
Licence: Apache-2.0.
