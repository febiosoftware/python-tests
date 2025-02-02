# @fbs {
#  "name" : "Create Box",
#  "info" : "This tool creates a box.",
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

# create the box
box = geom.GBox(int(W), int(H), int(D))
box.SetName("box1")
box.SetPosition(pos)

# add it to the active model
fem = mdl.GetActiveModel()
fem.AddObject(box)
