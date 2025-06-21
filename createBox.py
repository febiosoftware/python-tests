from fbs import *

# this is the function that will be called by FBS
def createBox(Width, Height, Depth, Position):
    fem = mdl.GetActiveModel()
    box = fem.AddBox(Width, Height, Depth)
    box.name = "box1"
    box.pos = Position

if __name__ == "__main__":
    createBox(1, 1, 1, core.vec3d(0,0,0))
    