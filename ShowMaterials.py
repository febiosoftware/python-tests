from fbs import *

def has_any(name, terms):
    name = name.lower()
    return any(term in name for term in terms)

def showMaterials(bone, skin, flesh, muscle):
    print("Starting engines ...")

    fem = post.active_model()
    nmat = len(fem.materials)
    print("There are " + str(nmat) + " materials.")

    for m in fem.materials:
        name = m.name
        if has_any(name, ["bone", "teeth", "clavicle", "sternum", "rib"]):
            m.visible = bone
        elif has_any(name, ["skin"]):
            m.visible = skin
        elif has_any(name, ["flesh", "cartilage"]):
            m.visible = flesh
        else:
            m.visible = muscle

    print("done")

if __name__ == "__main__":
    bone   = True
    skin   = True
    flesh  = True
    muscle = True
    showMaterials(bone, skin, flesh, muscle)
