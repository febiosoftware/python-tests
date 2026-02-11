from fbs import *

# Get the active model
fem = post.GetActiveModel()

# choose a data field to integrate
dataField = fem.GetDataField("stress")

# get the mesh
mesh = fem.GetFEMesh(0)

# get the element set to integrate over
elset = mesh.FindElemSet("Part1")

# loop over all states and integrate the data field over the element set
for state in range(0,fem.States()):
	val = post.IntegrateElements(fem, elset, dataField, post.MAT3DS.P1, state)
	print(state, val)
