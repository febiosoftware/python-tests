# @fbs { 
#  "name" : "Show Materials",
#  "info" : "This tool shows or hides tissues.",
#  "args" : {
#     "bone"   : { "type" : "bool", "value" : 1 },
#     "flesh"  : { "type" : "bool", "value" : 1 },
#     "skin"   : { "type" : "bool", "value" : 1 },
#     "muscle" : { "type" : "bool", "value" : 1 }
#  }
# }
from fbs import post, core, args
print("Starting engines ...")

showBone   = args['bone']
showFlesh  = args['flesh']
showSkin   = args['skin']
showMuscle = args['muscle']

fem = post.GetActiveModel()
nmat = fem.Materials()
print("There are " + str(nmat) + " materials.")

for i in range(nmat):
    m = fem.Material(i)
    name = m.name
    if ("bone" in name)or("Bone" in name)or("teeth" in name)or("Clavicle" in name)or("Sternum" in name)or("Rib" in name):
        if showBone:
            m.Show()
        else:
            m.Hide()
    elif ("skin" in name)or("Skin" in name):
        if showSkin:
            m.Show()
        else:
            m.Hide()
    elif ("flesh" in name)or("Flesh" in name)or("cartilage" in name)or("Cartilage" in name):
        if showFlesh:
            m.Show()
        else:
            m.Hide()
    else:
        if showMuscle:
            m.Show()
        else:
            m.Hide()

print("done")
