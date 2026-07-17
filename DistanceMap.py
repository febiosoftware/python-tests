# This script runs the distance map tool on a post model."
# (use co02.xplt for this example!)
from fbs import post

# get the active model
postModel = post.active_model()

# Get the mesh
mesh = postModel.fe_meshes[0]

# Here we get our selection for the first of the two surfaces and store it in surf1
surf1 = []
# We loop over all of the surfaces that are in the model
for surface in mesh.surfaces:
   
    # One of the contact surfaces is named "SecondarySurface01". If that's the one
    # that we're currently looking at, then set surf1 equal to that surface's list
    # of faces
    if surface.name == "SecondarySurface01":
        surf1 = surface.face_indices()

# Here, we just manually define our second surface. For this problem, we're just using
# a single face
surf2 = [135]

# Create the distance map field and evaluate it
distanceMap = post.DistanceMap(postModel, 0)
distanceMap.selection1 = surf1
distanceMap.selection2 = surf2
distanceMap.signed = False

# we need to assign it to the model
postModel.data_fields.add(distanceMap, "distance map")

# apply the map (This evaluates the distance map and updates the postModel's states)
distanceMap.apply()

# Here, we fill the state object with the correct data. The Evaluate function takes
# 3 arguments
#   the dataField
#   the component (because a distanceMap is a scalar data field it has no components
#       and so we put a 0 here)
#   the state that we want to get the data from. Here we get it from the last state
state = postModel.evaluate(distanceMap, 0, len(postModel.states) - 1)

# We loop over our first surface, and print the distanceMap data out for each facet
for index in surf1:
    print(state.faceData[index].val)
