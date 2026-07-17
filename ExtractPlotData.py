# This script extracts data from a post model.
# use co02.xplt as an example
from fbs import post

model = post.active_model()

# get the last state of the model
state = model.states[-1]

# evaluate the stress field
state.evaluate("stress", post.MAT3DS.P1)

# get the face data
faceData = state.face_data

mesh = state.fe_mesh
for surface in mesh.surfaces:
    print(surface.name)
    for face in surface.faces:
        print(str(face.id) + ", " + str(faceData[face.index].val))
