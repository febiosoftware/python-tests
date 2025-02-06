# @fbs {
#  "name" : "Create Simple Model",
#  "info" : "This tool creates a simple model.",
#  "args" : { 
#    "Width"  : 1, 
#    "Depth"  : 1, 
#    "Height" : 1, 
#    "position" : { "type" : "vec3", "value" : [0,0,0] } 
#  }
# }
from fbs import mdl, geom, args
W = args['Width']
H = args['Height']
D = args['Depth']
pos = args['position']

fem = mdl.GetActiveModel()

# create the box
box = fem.AddBox(int(W), int(H), int(D))
box.name = "box1"
box.pos = pos

# create a material
mat = fem.AddMaterial("Mat1", "neo-Hookean")

# assign it to the box
fem.AssignMaterial(box, mat)

# create a step
step = fem.AddStep("Step1", "solid")
