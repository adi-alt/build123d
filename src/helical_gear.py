from build123d import *
import os
import math

os.makedirs("exports", exist_ok=True)

teeth = 24
module = 2
thickness = 20

pitch_diameter = teeth * module
outer_diameter = pitch_diameter + 2 * module

with BuildPart() as gear:
    # Main gear body
    Cylinder(outer_diameter / 2, thickness)

    # Tooth cut pattern (simplified gear)
    for i in range(teeth):
        angle = 360 / teeth * i
        with Locations(Rot(0, 0, angle) * Pos(pitch_diameter / 2, 0, 0)):
            Box(module * 1.5, module * 4, thickness, mode=Mode.SUBTRACT)

    # Bore hole
    Cylinder(10, thickness + 2, mode=Mode.SUBTRACT)

model = gear.part

export_step(model, "exports/helical_gear.step")
export_stl(model, "exports/helical_gear.stl")
