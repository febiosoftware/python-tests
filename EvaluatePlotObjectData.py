# todo: this example doesn't work yet!!
import fbs

fem = fbs.active_post_model()

po = fem.plot_objects["Material2"]

data = po.data_fields["Force"]

print(po.name)

numStates = len(fem.states)
print(numStates)
for i in range(numStates):
	a = fem.evaluate_plot_object(po, data, 0, i)
	print(i, a)
