from fbs import *

fem = post.GetActiveModel()

po = fem.GetPlotObject("Material2")

data = po.GetDataField("Force")

print(po.Name())

numStates = fem.States()
print(numStates)
for i in range(numStates):
	a = fem.EvaluatePlotObject(po, data, 0, i)
	print(i, a)
