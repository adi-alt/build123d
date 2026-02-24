from build123d import *
import os

os.makedirs("exports", exist_ok=True)

length = 120
width = 80
height = 60
wall = 6

with BuildPart() as gearbox:
    Box(length, width, height)
    
    with Locations((0,0,0)):
        Box(length-wall*2, width-wall*2, height-wall*2, mode=Mode.SUBTRACT)

    # Bearing holes
    with Locations((0, width/2, 0), (0, -width/2, 0)):
        Cylinder(10, height+2, mode=Mode.SUBTRACT)

    # Mounting holes
    with GridLocations(length/2-10, width/2-10, 2, 2):
        Cylinder(4, height+2, mode=Mode.SUBTRACT)

model = gearbox.part
export_step(model, "exports/gearbox.step")
export_stl(model, "exports/gearbox.stl")