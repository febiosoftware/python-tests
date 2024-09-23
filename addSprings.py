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
from fbs import ui, core, args
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


def addSprings(Name, tol, File, Type, checkIntersect):
    springs = []
    
    ui.setProgressText("Reading springs from " + File)
    with open(File) as f:
        for line in f.readlines():
            springs.append(Spring(line))

    springSet = ui.SpringSet(Name, Type)
    
    
    ui.setProgressText("Adding springs to springset")
    index = 0
    for spring in springs:
        ui.setProgress(index/len(springs))
        index += 1

        if checkIntersect:
            ui.IntersectWithObject(spring.r0, spring.r1, tol)
    
        n1 = ui.FindOrMakeNode(spring.r0, tol)
        n2 = ui.FindOrMakeNode(spring.r1, tol)
        
        springSet.addSpring(n1, n2)

Name = args['name']
File = args['file']
tol  = args['tol']
type = args['Type']
intersect = args['intersect']
addSprings(Name, tol, File, type[1], intersect)
