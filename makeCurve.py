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
from fbs import ui, core, args
# Make Curve tool
def makeCurve(File, Radius, Divisions, Segments, Ratio):
    positions = []
    
    with open(File) as f:
        for line in f.readlines():
            splitCoords = line.split(",")
            
            x = float(splitCoords[0])
            y = float(splitCoords[1])
            z = float(splitCoords[2])
            
            positions.append(core.vec3d(x,y,z))
            
    ui.MeshFromCurve(positions, Radius, divisions=Divisions, segments=Segments, ratio=Ratio)

file = args['File']
radius = args['Radius']
divs = args['Division']
segs = args['Segments']
ratio = args['Ratio']
makeCurve(file, radius, divs, segs, ratio)
