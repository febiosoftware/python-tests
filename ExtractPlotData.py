#  This script extracts data from a post model."
from fbs import post

postModel = post.GetActiveModel()

dataField = postModel.GetDataField("stress")

# I think this changes the internal state of the post-model.
# Is this a problem?
state = postModel.Evaluate(dataField, post.MAT3DS.P1, postModel.States() - 1)

faceData = state.faceData

mesh = postModel.GetFEMesh(0)
for index in range(mesh.Surfaces()):
    surface = mesh.Surface(index)
    print(surface.GetName())
    faces = surface.GetFaceIndices()
    for face in faces:
        print(str(face) + ", " + str(faceData[face].val))
