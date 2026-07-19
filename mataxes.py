import fbs

mdl = fbs.active_model()

o = mdl.objects[0]

m = o.fe_mesh

x = m.data_field[0]
y = m.data_field[1]

for i in range(0, len(m.elements)):
    a = x.get_vec3(i)
    b = y.get_vec3(i)

    el = m.element(i)
    el.set_axes(a, b)
