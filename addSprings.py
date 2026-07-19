# Add Springs tool
# Open the leaflets.vtk file first. 
# Then use the chordae.csv file to read the springs
from dataclasses import dataclass
import csv
import fbs
from fbs import core, mesh

@dataclass
class Spring:
    r0: core.Vec3
    r1: core.Vec3

def read_springs(filename):
    springs = []

    with open(filename, newline="") as f:
        for row in csv.reader(f):
            springs.append(Spring(
                core.Vec3(float(row[1]), float(row[2]), float(row[3])),
                core.Vec3(float(row[4]), float(row[5]), float(row[6])),
            ))

    return springs

def closest_node_index(positions, r, tol):
    tol2 = tol * tol
    best = min(
        enumerate(positions),
        key=lambda item: (r - item[1]).sqr_length(),
        default=None,
    )

    if best is None:
        return None

    index, pos = best
    return index if (r - pos).sqr_length() < tol2 else None

def find_or_add_node(obj, positions, r, tol):
    index = closest_node_index(positions, r, tol)
    if index is not None:
        return obj.get_or_create_geometry_node(index)

    return obj.add_node(r)

def intersect_with_object(obj, r0, r1, tol):
    direction = (r1 - r0).normalized()

    for q in mesh.find_all_intersections(obj.fe_mesh, r0, direction, True):
        if (q - r0).length() < tol and (r1 - q).length() < (r1 - r0).length():
            r0 = q

    for q in mesh.find_all_intersections(obj.fe_mesh, r1, -direction, True):
        if (q - r1).length() < tol and (q - r0).length() < (r1 - r0).length():
            r1 = q

    return r0, r1

def add_springs(o, name, file, tol, typeName, intersect):

    fem = fbs.active_model()
    spring_set = fem.discrete_objects.add_spring_set(name, typeName)
    
    T = o.transform
    
    print("collecting nodal positions ...")
    node_positions = [T.local_to_global(node.pos) for node in o.fe_mesh.nodes]
    
    print("creating springs ...")
    for spring in read_springs(file):
        r0, r1 = spring.r0, spring.r1

        if intersect:
            r0, r1 = intersect_with_object(o, r0, r1, tol)

        n1 = find_or_add_node(o, node_positions, r0, tol)
        n2 = find_or_add_node(o, node_positions, r1, tol)

        spring_set.springs.add(n1, n2)


if __name__ == "__main__":

    fem = fbs.active_model()
    fem.clear()
    
    print("importing file ...")
    o = fem.objects.import_file("leaflets.vtk")

    fileName = "chordae.csv" 

    add_springs(o, "springs", fileName, 0.1, "Linear", False)


