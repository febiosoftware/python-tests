# @fbs { 
#  "name" : "Material color",
#  "info" : "This tool sets material colors.",
#  "args" : {
#     "bone"   : { "type" : "color", "value" : [210, 200, 200] },
#     "flesh"  : { "type" : "color", "value" : [200, 200, 100] },
#     "skin"   : { "type" : "color", "value" : [255, 200, 200] },
#     "muscle" : { "type" : "color", "value" : [150,  50,  50] }
#  }
# }
from fbs import post, core, args
print("Starting engines ...")

fem = post.GetActiveModel()
nmat = fem.Materials()
print("There are " + str(nmat) + " materials.")

col_bone = args['bone']
col_flesh = args['flesh']
col_skin = args['skin']
col_muscle = args['muscle']

for i in range(nmat):
    m = fem.Material(i)
    name = m.name
    if ("skin" in name)or("Skin" in name):
        m.SetColor(col_skin.r, col_skin.g, col_skin.b)
    elif ("bone" in name)or("Bone" in name)or("teeth" in name)or("Clavicle" in name)or("Sternum" in name)or("Rib" in name):
        m.SetColor(col_bone.r, col_bone.g, col_bone.b)
    elif ("flesh" in name)or("Flesh" in name)or("cartilage" in name)or("Cartilage" in name):
        m.SetColor(col_flesh.r, col_flesh.g, col_flesh.b)
    else:
        m.SetColor(col_muscle.r, col_muscle.g, col_muscle.b)

print("done")
