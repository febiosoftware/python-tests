import sys
import fbs

# 1. this opens the plot file and returns an object that contains the data
model = fbs.post_models.open("co02.xplt")

# 2. the following is optional, but in case you want to see what fields are stored in the plot file
print(f"Number of data fields: {len(model.data_fields)}")

if not model.data_fields:
    print("hmm, something is not right ...\n")
    sys.exit(1)

for df in model.data_fields:
    print(df.name)

# 3. extract data and print it
# evaluate the datafield on the model. Returns a state object that contains the data
state = model.states[-1]
state.evaluate(("Lagrange strain", "effective"))

# retrieve the state's element data
elemData = state.elem_data

# retrieve the FE mesh
mesh = state.fe_mesh

# output the data for each element
for elem in mesh.elements:
    print(str(elem.id) + ", " + str(elemData[elem.index].val))
