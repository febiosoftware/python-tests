from fbs import *

def createSimpleModel(Width, Height, Depth, position):

    fem = mdl.GetActiveModel()

    # create the box
    box = fem.AddBox(Width, Height, Depth)
    box.name = "box1"
    box.pos = position

    # create a material
    mat = fem.AddMaterial("Mat1", "neo-Hookean")

    # assign it to the box
    fem.AssignMaterial(box, mat)

    # create a step
    step = fem.AddStep("Step1", "solid")

if __name__ == "__main__":
    createSimpleModel(1,1,1, core.vec3d(0,0,0))
    