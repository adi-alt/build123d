from build123d import *
import os

os.makedirs("exports", exist_ok=True)

length = 150
width = 100
height = 60
wall = 4

with BuildPart() as enclosure:
    # Outer box
    Box(length, width, height)

    # Hollow interior
    Box(length - wall*2, width - wall*2, height - wall*2, mode=Mode.SUBTRACT)

    # Vent slots (CORRECT WAY)
    with BuildSketch(Plane.XY.offset(height/2 - wall/2)):
        with GridLocations(15, 10, 6, 4):
            SlotOverall(20, 4)

    extrude(amount=wall + 2, mode=Mode.SUBTRACT)

    # Screw bosses
    with GridLocations(length/2 - 15, width/2 - 15, 2, 2):
        Cylinder(5, height/2)

model = enclosure.part

export_step(model, "exports/enclosure.step")
export_stl(model, "exports/enclosure.stl")
