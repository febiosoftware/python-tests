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
from fbs import mdl, geom, mesh, core, args, ui

# get the tool's arguments
file = args['File']
radius = args['Radius']
divs = args['Division']
segs = args['Segments']
ratio = args['Ratio']

# read the points from a file
def readPositionsFromFile(filename):
    positions = []
    with open(filename) as f:
        for line in f.readlines():
            splitCoords = line.split(",")
            x = float(splitCoords[0])
            y = float(splitCoords[1])
            z = float(splitCoords[2])
        
            positions.append(core.vec3d(x,y,z))
    return positions

def meshFromCurve(points, radius, ndiv, nseg, ratio):
    disc = geom.GDisc(radius)
    discMesh = disc.CreateMesh(ndiv, nseg, ratio)

    nodePositions = []
    for point in range(0, len(points)):
        # Rotate the disc 
        if point == 0:
            vec1 = core.vec3d(0,0,1)
            vec2 = (points[point + 1] - points[point]).Normalize()
            disc.GetTransform().Rotate(core.quatd(vec1, vec2), core.vec3d(0,0,0))
        elif (point != len(points) - 1):
            vec1 = (points[point] - points[point - 1]).Normalize()
            vec2 = (points[point + 1] - points[point]).Normalize()
            disc.GetTransform().Rotate(core.quatd(vec1, vec2), points[point - 1])

        # Move the disc into position
        disc.SetPosition(points[point])

        # Add all of the node locations to our vector
        for node in range(0, discMesh.Nodes()):
            nodePositions.append(discMesh.NodePosition(node))

    newMesh = mesh.Mesh()
    newMesh.Create(len(nodePositions), discMesh.Elements() * (len(points) - 1), 0, 0)

    for node in range(0, newMesh.Nodes()):
        newMesh.Node(node).pos = nodePositions[node]

    for point in range(0, len(points) - 1):
        ui.panels.pytools.SetProgress(point/len(points))
        for element in range(0, discMesh.Elements()):
            # For each element, grab the corresponding element from the disc mesh so 
            # that we can use that node connectivity.
            discElement = discMesh.Element(element)

            # The current element on our new mesh corresponds to an element on the disc
            # mesh, but is offset by the number of elements in the disc mesh times the 
            # number of previous points in our curve
            eid = element + discMesh.Elements() * point
            current = newMesh.Element(eid)
            current.SetType(mesh.ElementType.FE_HEX8)

            for node in range(0, discElement.Nodes()):
                # Grab the node number from the disc element, but them offset it by the 
                # number of nodes that were used in previous points in our curve
                current.SetNode(node, discElement.Node(node) + discMesh.Nodes() * point)

                # Here we do the same, but the node in question lies on the next point, as it's
                # on the far face of the hex element
                current.SetNode(node + discElement.Nodes(), discElement.Node(node) + discMesh.Nodes() * (point + 1))

    newMesh.RebuildMesh(60.0, False)
    return newMesh

positions = readPositionsFromFile(file)

# create a new mesh
mesh = meshFromCurve(positions, radius, divs, segs, ratio)

# construct a mesh-object
o = geom.GMeshObject(mesh)
o.SetName("curve")

# add it to the model
mdl.AddObject(o)
