# this will import all fbs modules
# This file needs mdl, core, geom
from fbs import *

# Get the currently active (build) model 
fem = mdl.GetActiveModel()

# import an object from a file
o = fem.ImportGeometryFromFile("skull.vtp")

# Get the object's transform, which controls its location in space
T = o.GetTransform()

# Set the position of the object
T.SetPosition(core.vec3d(0,0,1))

# Set its orientation using Euler angles (in degrees!)
T.SetEulerAngles(90, 0, 0)
