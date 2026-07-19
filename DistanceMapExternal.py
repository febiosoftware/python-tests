from fbs import post

# Open the file
postModel = post.read_plot_file("co02.xplt")

# Get the mesh
mesh = postModel.fe_meshes[0]

# we need two surfaces to run the distance map tool. The first surface is defined by a surface name.
surf1 = mesh.surfaces["SecondarySurface01"]

# Here, we just manually define our second surface. For this problem, we're just using
# a single face
surf2 = mesh.faces[135]

# Create the distance map field and evaluate it
distanceMap = postModel.data_fields.add("Map1", "distance map")
distanceMap.selection1 = surf1
distanceMap.selection2 = surf2
distanceMap.signed = False

# this calculates the distance map for all the states of the model.
distanceMap.apply()

# retrieve the last state of the model and evaluate the distance map field
state = postModel.states[-1]
state.evaluate("Map1")

# We loop over our first surface, and print the distanceMap data out for each facet
for face in surf1.faces:
    print(state.face_data[face.index].val)
