from fbs import *

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

# this is the function that creates the curve
def makeCurve(file, radius, divisions, segments, ratio):
    print("Reading points from file: " + file)
    points = readPositionsFromFile(file)

    model = mdl.active_model()
    model.clear()

    disc = model.objects.add("tmp", "disc", R=radius)
    disc.build_fe_mesh(nd=divisions, nr=segments, r=ratio)

    T = disc.transform

    print("Creating points along curve...")
    nodePositions = []
    for point in range(0, len(points)):
        # Rotate the disc 
        if point == 0:
            vec1 = core.vec3d(0,0,1)
            vec2 = (points[point + 1] - points[point]).Normalize()
            T.rotate(core.quatd(vec1, vec2), core.vec3d(0,0,0))
        elif (point != len(points) - 1):
            vec1 = (points[point] - points[point - 1]).Normalize()
            vec2 = (points[point + 1] - points[point]).Normalize()
            T.rotate(core.quatd(vec1, vec2), points[point - 1])

        # Move the disc into position
        T.position = points[point]

        # Add all of the node locations to our vector
        discMesh = disc.fe_mesh
        for node in discMesh.nodes:
            nodePositions.append(T.local_to_global(node.pos))

    # create a new mesh object
    meshObject = model.objects.add_mesh_object("curve")
    newMesh = meshObject.fe_mesh

    print("Creating mesh...")
    newMesh.create(len(nodePositions), len(discMesh.elements) * (len(points) - 1), 0, 0)

    for node in newMesh.nodes:
        node.pos = nodePositions[node.index]

    numDiscNodes = len(discMesh.nodes)
    numDiscElements = len(discMesh.elements)

    for point in range(0, len(points) - 1):
        for element in range(0, numDiscElements):
            # For each element, grab the corresponding element from the disc mesh so 
            # that we can use that node connectivity.
            discElement = discMesh.elements[element]

            # The current element on our new mesh corresponds to an element on the disc
            # mesh, but is offset by the number of elements in the disc mesh times the 
            # number of previous points in our curve
            eid = element + numDiscElements * point
            current = newMesh.elements[eid]
            current.set_type(mesh.ElementType.FE_HEX8)

            nelNodes = len(discElement.nodes)

            disc_nodes = discElement.nodes
            current_nodes = current.nodes

            base0 = numDiscNodes * point
            base1 = numDiscNodes * (point + 1)

            for node in range(0, nelNodes):
                src = disc_nodes[node] 
                # Grab the node number from the disc element, but them offset it by the 
                # number of nodes that were used in previous points in our curve
                current_nodes[node] = src + base0

                # Here we do the same, but the node in question lies on the next point, as it's
                # on the far face of the hex element
                current_nodes[node + nelNodes] = src + base1

    newMesh.rebuild_mesh(60.0, False)
    meshObject.update_geometry()

    # Remove the disc from the model, since we don't need it anymore
    model.objects.remove(disc)

    print("Done! Created " + str(len(nodePositions)) + " nodes and " + str(len(newMesh.elements)) + " elements.")


if __name__ == "__main__":
    fileName = "MarkupsCurve_1.csv"
    makeCurve(fileName, 1.0, 4, 5, 0.5)
