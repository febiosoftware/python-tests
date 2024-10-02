# @fbs {
#  "name" : "Make Curve",
#  "info" : "This tool creates a solid mesh from a curve",
#  "args" : {
#    "File" : { "type" : "url", "value" : "" },
#    "Radius" : 1,
#    "Division" : { "type" : "int", "value" : 4 },
#    "Segments" : { "type" : "int", "value" : 4 },
#    "Ratio" : 0.5
#  }
# }
from fbs import mdl, core, args

# get the tool's arguments
file = args['File']
radius = args['Radius']
divs = args['Division']
segs = args['Segments']
ratio = args['Ratio']

# read the points from a file
positions = []
with open(file) as f:
    for line in f.readlines():
        splitCoords = line.split(",")
        x = float(splitCoords[0])
        y = float(splitCoords[1])
        z = float(splitCoords[2])
        
        positions.append(core.vec3d(x,y,z))

# create a new mesh
mesh = mdl.mesh_from_curve(positions, radius, divs, segs, ratio)

# construct a mesh-object
o = mdl.create_mesh_object("curve", mesh)

# get the currently active model
gm = mdl.active_model()

# add it to the model
gm.add_object(o)
