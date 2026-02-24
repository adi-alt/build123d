from build123d import *
import os

os.makedirs("exports", exist_ok=True)

thickness = 8
width = 80
height = 100

with BuildPart() as bracket:
    with BuildSketch(Plane.XY):
        Rectangle(width, thickness)
    extrude(amount=height)

    with BuildSketch(Plane.YZ):
        Rectangle(height, thickness)
    extrude(amount=width)

    # Bolt holes
    with GridLocations(60, 60, 2, 2):
        Cylinder(6, thickness+20, mode=Mode.SUBTRACT)

model = bracket.part
export_step(model, "exports/bracket.step")
export_stl(model, "exports/bracket.stl")