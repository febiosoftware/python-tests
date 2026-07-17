# This tool demonstrates how to set the material colors in a post model.
from fbs import *

def setMaterialColors(bone, flesh, skin, muscle):
    print("Starting engines ...")

    fem = post.active_model()
    nmat = len(fem.materials)
    print("There are " + str(nmat) + " materials.")

    for material in fem.materials:
        name = material.name.lower()

        if "skin" in name:
            material.color = skin
        elif any(term in name for term in ["bone", "teeth", "clavicle", "sternum", "rib"]):
            material.color = bone
        elif any(term in name for term in ["flesh", "cartilage"]):
            material.color = flesh
        else:
            material.color = muscle

    print("done")

if __name__ == "__main__":
    bone   = core.color(210, 200, 200)
    flesh  = core.color(200, 200, 100)
    skin   = core.color(255, 200, 200)
    muscle = core.color(150,  50,  50)
    setMaterialColors(bone, flesh, skin, muscle)
    