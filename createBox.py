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
from fbs import ui, args
W = args['Width']
H = args['Height']
D = args['Depth']
pos = args['position']
ui.GBox(pos, W, H, D)
