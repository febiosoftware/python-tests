import sys
from fbs import post, core

# Open the plot file and get an object that contains the data
postModel = post.ReadPlotFile("co02.xplt")

# configure the vtk writer
vtk = post.vtkExport()
vtk.ExportAllStates(True) # this will write all states
vtk.WriteSeriesFile(True) # this will create a vtk series file

# save to file(s)
vtk.Save(postModel, "output.vtk")
