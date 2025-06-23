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

# this is the function that will be called by the tool
def readCurve(file, closeCurve):
    positions = readPositionsFromFile(file)

    # create a new curve mesh
    curveMesh = mesh.CurveMesh()
    curveMesh.CreateFromPoints(positions, closeCurve)

    # get the active model
    fem = mdl.GetActiveModel()

    # construct a mesh-object
    curve = fem.AddCurveMeshObject(curveMesh)
    curve.name = "CurveObject"


if __name__ == "__main__":
    file = "MarkupsCurve_1.csv"
    readCurve(file, False)
