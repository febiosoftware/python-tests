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
from fbs import ui, mdl, core, mesh, args
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

# get all the nodes of the object's mesh
# in global coordinates
def GetAllNodes(o):
    m = o.GetFEMesh()
    N = m.Nodes()
    allNodes = []
    for i in range(0,N):
        ni = m.Node(i)
        ri = m.LocalToGlobal(ni.pos)
        allNodes.append(ri)
    return allNodes

# finds the closest node (or -1 if not found)
def FindClosestNode(nodeList, r, tol):
    N = len(nodeList)
    imin = -1
    l2min = 0.0
    for i in range(0,N):
        ri = nodeList[i]
        l2 = (r - ri).SqrLength()
        if (imin == -1) or (l2 < l2min):
            imin = i
            l2min = l2

    if (imin != -1) and (l2min < tol*tol):
        return imin
    
    return -1

# This function finds the closest node on the object's mesh (using the pre-calculated node position list).
# If it exists, then it's marked as a required node. If not, it gets added to the object.
def FindOrMakeGNode(o, nodeList, r, tol):
    N = len(nodeList)
    imin = FindClosestNode(nodeList, r, tol)

    if (imin != -1):
        return o.MakeGNode(imin)
    
    return o.AddNode(r)

def IntersectWithObject(o, r0, r1, tol):
    femesh = o.GetFEMesh()

    n = r1 - r0
    n.Normalize()

    intersections = mesh.FindAllIntersections(femesh, r0, n, True)
    for i in range(0, len(intersections)):
        q = intersections[i]

        # does the projection lie within tolerance
        d = (q - r0).Length()
        if d < tol:
            # does it decrease the distance
            if ((r1 - q).Length() < (r1 - r0).Length()):
                r0 = q

    intersections = mesh.FindAllIntersections(femesh, r1, -n, True)
    for i in range(0, len(intersections)):
        q = intersections[i]

        # does the projection lie within tolerance
        d = (q - r1).Length()
        if (d < tol):
            # does it decrease the distance
            if ((q - r0).Length() < (r1 - r0).Length()):
                r1 = q

name = args['name']
file = args['file']
tol  = args['tol']
type = args['Type']
intersect = args['intersect']
typeStr = type[1]

springs = []

ui.panels.pytools.SetProgressText("Reading springs from " + file)
with open(file) as f:
    for line in f.readlines():
        springs.append(Spring(line))

springSet = mdl.AddSpringSet(name, typeStr)

# get the currently selected object
o = mdl.GetActiveObject()

allNodes = GetAllNodes(o)

ui.panels.pytools.SetProgressText("Adding springs to springset")
index = 0
for spring in springs:
    ui.panels.pytools.SetProgress(index/len(springs))
    index += 1

    if intersect:
        IntersectWithObject(o, spring.r0, spring.r1, tol)

    n1 = FindOrMakeGNode(o, allNodes, spring.r0, tol)
    n2 = FindOrMakeGNode(o, allNodes, spring.r1, tol)
    
    springSet.AddSpring(n1, n2)
