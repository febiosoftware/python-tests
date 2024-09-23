from fbs import core

def curveTest(File, Radius, Divisions, Segments, Ratio):
    positions = []
    
    with open(File) as f:
        for line in f.readlines():
            splitCoords = line.split(",")
            
            x = float(splitCoords[0])
            y = float(splitCoords[1])
            z = float(splitCoords[2])
            
            positions.append(core.vec3d(x,y,z))
            
    core.curveToVTKMesh(positions, Radius, "curve.vtk", Divisions, Segments, Ratio)
            

curveTest("C:/Users/Steve/Documents/Python Scripts/Python/Python/PDA/MarkupsCurve_1.csv", 1.0, 4, 4, 0.5)



