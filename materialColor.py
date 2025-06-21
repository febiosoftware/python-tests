# This tool demonstrates how to set the material colors in a post model.
from fbs import *

def setMaterialColors(bone, flesh, skin, muscle):
    print("Starting engines ...")

    fem = post.GetActiveModel()
    nmat = fem.Materials()
    print("There are " + str(nmat) + " materials.")

    for i in range(nmat):
        m = fem.Material(i)
        name = m.name
        if ("skin" in name)or("Skin" in name):
            m.SetColor(skin.r, skin.g, skin.b)
        elif ("bone" in name)or("Bone" in name)or("teeth" in name)or("Clavicle" in name)or("Sternum" in name)or("Rib" in name):
            m.SetColor(bone.r, bone.g, bone.b)
        elif ("flesh" in name)or("Flesh" in name)or("cartilage" in name)or("Cartilage" in name):
            m.SetColor(flesh.r, flesh.g, flesh.b)
        else:
            m.SetColor(muscle.r, muscle.g, muscle.b)

    print("done")

if __name__ == "__main__":
    bone   = core.color(210, 200, 200)
    flesh  = core.color(200, 200, 100)
    skin   = core.color(255, 200, 200)
    muscle = core.color(150,  50,  50)
    setMaterialColors(bone, flesh, skin, muscle)
    