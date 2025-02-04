from fbs import *

model = post.GetActiveModel()

mesh = model.GetFEMesh(0)

state = model.

NN = mesh.Nodes()

print(NN)

for i in range(0,NN):
	r = mesh.


