from fbs import post

# Get the active model
fem = post.active_model()
#fem = post.read_plot_file("Model1.xplt")

# loop over all states and integrate the data field over the element set
for state in fem.states:
	val = state.integrate_elements("Part1", ("stress", "p1"))
	print(state.time, val)
