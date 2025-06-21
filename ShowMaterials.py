from fbs import *

def showMaterials(bone, skin, flesh, muscle):
    print("Starting engines ...")

    fem = post.GetActiveModel()
    nmat = fem.Materials()
    print("There are " + str(nmat) + " materials.")

    for i in range(nmat):
        m = fem.Material(i)
        name = m.name
        if ("bone" in name)or("Bone" in name)or("teeth" in name)or("Clavicle" in name)or("Sternum" in name)or("Rib" in name):
            if bone:
                m.Show()
            else:
                m.Hide()
        elif ("skin" in name)or("Skin" in name):
            if skin:
                m.Show()
            else:
                m.Hide()
        elif ("flesh" in name)or("Flesh" in name)or("cartilage" in name)or("Cartilage" in name):
            if flesh:
                m.Show()
            else:
                m.Hide()
        else:
            if muscle:
                m.Show()
            else:
                m.Hide()

    print("done")

if __name__ == "__main__":
    bone   = True
    skin   = True
    flesh  = True
    muscle = True
    showMaterials(bone, skin, flesh, muscle)
