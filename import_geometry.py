import fbs

# Get the currently active (build) model 
fem = fbs.active_model()

# import an object from a file
skull = fem.objects.import_file("skull.vtp")

# Get the object's transform, which controls its location in space
transform = skull.transform

# Set the position of the object
transform.position = (0,0,1)

# Set its orientation using Euler angles (in degrees!)
transform.set_euler_angles_deg(90, 0, 0)
