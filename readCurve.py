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

    print("Reading points ...")
    positions = readPositionsFromFile(file)
    print(f"{len(positions)} points read.")

    # get the active model
    fem = mdl.active_model()
    fem.clear()

    # construct a curve mesh-object
    o = fem.objects.add_curve_mesh_object("CurveObject")
    curveMesh = o.geometry_mesh

    print("building curve mesh ...")
    curveMesh.create_from_points(positions, closeCurve)
    o.update_geometry()
    print("Done!")


if __name__ == "__main__":
    file = "MarkupsCurve_1.csv"
    readCurve(file, False)
