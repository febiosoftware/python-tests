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

# define the tool's properties
props = {}
props['file'] = "@url:"
props['closeCurve'] = False

# add the tool
ui.panels.pytools.AddTool("Read Curve", props, readCurve, "This tool reads a curve from a file.")
