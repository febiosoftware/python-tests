from fbs import *

#define the tool's properties
props = {}
props['Width'] = 1.0
props['Height'] = 1.0
props['Depth'] = 1.0
props['Position'] = core.vec3d(0,0,0)

# this is the function that will be called by FBS
def applyTool(Width, Height, Depth, Position):
    fem = mdl.GetActiveModel()
    box = fem.AddBox(Width, Height, Depth)
    box.name = "box1"
    box.pos = Position

# add the tool to the UI
ui.panels.pytools.AddTool("Create Box", props, applyTool)
