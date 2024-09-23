# @fbs { 
#  "name" : "My first tool",
#  "info" : "This is an example of a tool.",
#  "args" : { "width" : 1, "height" : 1, "depth" : 1 }
# }
from fbs import mdl, core, args
print("Starting engines ...")

#position of box
pos = core.vec3d(0,0,0)

# create the box
print("Creating box ...")
o = mdl.CreateBox("box1", pos, args['width'], args['height'], args['depth'])

# mesh it
print("Building mesh ...")
o.BuildMesh()

# add a material
print("Adding material ...")
m = mdl.AddMaterial("mat1", "neo-Hookean")
m.set("E", 1.0)
m.set("v", 0.3)

#assign it to the object
print("Assigning material ...")
o.AssignMaterial(m)

# add a step
print("Adding step ...")
mdl.AddStep("Step1")

print("Exporting model ...")
b = mdl.ExportFEB("C:/Users/Steve/Documents/Python Scripts/Python/Python/py.feb")
if b:
    print("Output was a success!")
else:
    print("I'm sorry to report that your request was met with complete failure.")
