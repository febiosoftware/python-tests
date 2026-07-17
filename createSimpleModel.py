# NOTE: To run this script, open FEBio Studio and start a new model. Then, use the menu **Tools --> Python Editor** to open the Python editor window.
#       Then, copy/paste this code in the editor and run it.

from fbs import mdl

# get the active model
fem = mdl.active_model()
#fem.clear()

# add a box to the model
box = fem.objects.add("Box1", "box", w=1.0, h=1.0, d=1.0)

# generate mesh
box.build_fe_mesh(nx=5, ny=5, nz=5)

# add a material to the model
mat = fem.materials.add("Mat1", "neo-Hookean", E=100, v=0.3)

# assign the material to the part
box.assign_material(mat)

# create a load curve (for the prescribed displacement below)
lc = fem.load_controllers.add("LC1", "loadcurve", points=[(0,0), (1,1)])

# get the initial step
step0 = fem.steps.initial # this always points to fem.steps[0]

# create the zero displacement BC
bc1 = step0.boundary_conditions.add("BC1", "zero displacement", x_dof = True, y_dof = True, z_dof = True)

# create the prescribed displacement BC
bc2 = step0.boundary_conditions.add("BC2", "prescribed displacement", dof=0, value = 1.0)

# assign load controller to the "value" parameter
bc2.params["value"].lc = lc

# create two selections
sel1 = fem.selections.add("left_surface", box.surfaces[3])
sel2 = fem.selections.add("right_surface", box.surfaces[1])

# set the boundary conditions' selections
bc1.selection = sel1
bc2.selection = sel2

# add analysis step
step1 = fem.steps.add("Step1", "solid", time_steps=20, step_size=0.05)

# add a plot variable
fem.plot_variables.add("Lagrange strain")
