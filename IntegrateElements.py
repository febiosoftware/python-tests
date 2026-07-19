import fbs

# Get the active model
fem = fbs.active_post_model()
#fem = fbs.read_plot_file("Model1.xplt")

# loop over all states and integrate the data field over the element set
for state in fem.states:
	val = state.integrate_elements("Part1", ("stress", "p1"))
	print(state.time, val)
