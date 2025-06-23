from fbs import post

# Open the file
postModel = post.ReadPlotFile("co02.xplt")

# Get the mesh
mesh = postModel.GetFEMesh(0)

# Here we get our selection for the first of the two surfaces and store it in surf1
surf1 = []
# We loop over all of the surfaces that are in the model
for index in range(mesh.Surfaces()):
    surface = mesh.Surface(index)
    
    # One of the contact surfaces is named "SecondarySurface01". If that's the one
    # that we're currently looking at, then set surf1 equal to that surface's list
    # of faces
    if surface.GetName() == "SecondarySurface01":
        surf1 = surface.GetFaceIndices()

# Here, we just manually define our second surface. For this problem, we're just using
# a single face
surf2 = [135]

# Create the distance map field and evaluate it
distanceMap = post.DistanceMap(postModel, 0)
distanceMap.SetSelection1(surf1)
distanceMap.SetSelection2(surf2)
distanceMap.SetSigned(False)

# we need to assign it to the model
postModel.AddDataField(distanceMap, "distance map")

# apply the map (This evaluates the distance map and updates the postModel's states)
distanceMap.Apply()

# Here, we fill the state object with the correct data. The Evaluate function takes
# 3 arguments
#   the dataField
#   the component (because a distanceMap is a scalar data field it has no components
#       and so we put a 0 here)
#   the state that we want to get the data from. Here we get it from the last state
state = postModel.Evaluate(distanceMap, 0, postModel.States() - 1)

# We loop over our first surface, and print the distanceMap data out for each facet
for index in surf1:
    print(state.faceData[index].val)
