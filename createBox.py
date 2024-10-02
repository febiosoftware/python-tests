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
from fbs import mdl, args
W = args['Width']
H = args['Height']
D = args['Depth']
pos = args['position']

box = mdl.create_box("box1", pos, W, H, D)
gm = mdl.active_model()
gm.add_object(box)
