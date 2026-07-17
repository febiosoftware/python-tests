from fbs import post, core

# Open the plot file and get an object that contains the data
postModel = post.read_plotfile("co02.xplt")

# configure the vtk writer
vtk = post.VTKExport()
vtk.export_all_states = True # this will write all states
vtk.write_series_file = True # this will create a vtk series file

# save to file(s)
vtk.save(postModel, "tmp/output.vtk")
