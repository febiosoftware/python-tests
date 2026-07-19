# This tool demonstrates how to set the material colors in a post model.
import fbs

def setMaterialColors(bone, flesh, skin, muscle):
    print("Starting engines ...")

    fem = fbs.active_post_model()
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
    bone   = fbs.core.Color(210, 200, 200)
    flesh  = fbs.core.Color(200, 200, 100)
    skin   = fbs.core.Color(255, 200, 200)
    muscle = fbs.core.Color(150,  50,  50)
    setMaterialColors(bone, flesh, skin, muscle)
