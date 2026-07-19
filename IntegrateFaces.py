import fbs

# get the active model
fem = fbs.active_post_model()
#fem = fbs.read_plot_file("Model1.xplt")

# loop over all states and integrate the data field over the surface
for state in fem.states:
	val = state.integrate_faces("SlidingElastic1Primary", "contact pressure")
	print(state.time, val)

