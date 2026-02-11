from fbs import *

# get the active model
fem = post.GetActiveModel()

# choose a data field to integrate
dataField = fem.GetDataField("test")

# get the mesh
mesh = fem.GetFEMesh(0)

# get the surface to integrate over
surf = mesh.FindSurface("Surface01")

# loop over all states and integrate the data field over the surface
for state in range(0,fem.States()):
	val = post.IntegrateFaces(fem, surf, dataField, 0, state)
	print(state, val)
