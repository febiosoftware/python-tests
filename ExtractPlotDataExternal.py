import sys
from fbs import post, core

# 1. this opens the plot file and returns an object that contains the data
postModel = post.ReadPlotFile("co02.xplt")

# 2. the following is optional, but in case you want to see what fields are stored in the plot file
# get the data manager 
manager = postModel.GetDataManager()

nrfields = manager.DataFields()
print("Number of datafields : " + str(nrfields))
if (nrfields == 0):
    print("hmm, something is not right ...\n")
    sys.exit(1)

for i in range(manager.DataFields()):
    df = manager.DataField(i)
    print(df.name)

# 3. extract data and print it
# get a handle to retrieve a particular data field
dataField = postModel.GetDataField("Lagrange strain")

# evaluate the datafield on the model. Returns a state object that contains the data
state = postModel.Evaluate(dataField, post.MAT3DS.EFFECTIVE, postModel.States() - 1)

# retrieve the state's element data
elemData = state.elemData

# retrieve the mesh
mesh = postModel.GetFEMesh(0)

# output the data for each element
for index in range(mesh.Elements()):
    print(str(index) + ", " + str(elemData[index].val))
