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

# Build the tool's property list
props = {}
props['Width'] = 1.0
props['Height'] = 1.0
props['Depth'] = 1.0
props['position'] = core.vec3d(0,0,0)

# add the tool
ui.panels.pytools.AddTool("Simple Model", props, createSimpleModel, "Create a simple model.")
