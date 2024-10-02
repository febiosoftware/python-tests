# @fbs {
#   "name" : "Add Springs",
#   "info" : "This tool adds some springs",
#   "args" : {
#      "name" : "",
#      "file" : { "type" : "url", "value" : "" },
#      "tol" : 0.1,
#      "Type" : { "type" : "enum", "value" : ["Linear", "Nonlinear", "Hill"] },
#      "intersect" : { "type" : "bool", "value" : 0 }
#    }
# }
from fbs import ui, mdl, core, args
# Add Springs tool

class Spring:
    
    def __init__(self, coords):
        splitCoords = coords.split(",")
        
        x = float(splitCoords[1])
        y = float(splitCoords[2])
        z = float(splitCoords[3])
        
        self.r0 = core.vec3d(x,y,z)
        
        x = float(splitCoords[4])
        y = float(splitCoords[5])
        z = float(splitCoords[6])
        
        self.r1 = core.vec3d(x,y,z)

Name = args['name']
File = args['file']
tol  = args['tol']
type = args['Type']
intersect = args['intersect']
Type = type[1]

springs = []

ui.panels.pytools.set_progress_text("Reading springs from " + File)
with open(File) as f:
    for line in f.readlines():
        springs.append(Spring(line))

springSet = mdl.SpringSet(Name, Type)

ui.panels.pytools.set_progress_text("Adding springs to springset")
index = 0
for spring in springs:
    ui.panels.pytools.set_progress(index/len(springs))
    index += 1

    if intersect:
        mdl.intersect_with_object(spring.r0, spring.r1, tol)
    
    n1 = mdl.find_or_make_node(spring.r0, tol)
    n2 = mdl.find_or_make_node(spring.r1, tol)
        
    springSet.add_spring(n1, n2)
