# Simple tool for testing various input fields. 
from fbs import *

# output the values
def outputValues(FILE, name, doubleVal, intVal, boolVal, vector, choice):
    print("Checkbox checked: " + str(boolVal))
    print("Integer value: " + str(intVal))
    print("Double value: " + str(doubleVal))
    print("Length of vector: " + str(vector.Length()))
    print("My name is " + name)
    if len(FILE)==0:
        print("No FILE specified.")
    else:
        print("The file says:")
        with open(FILE, "r") as f:
            for line in f:
                print("\t" + line.strip())

    print("The index of the selected drop-down item was " + str(choice[0]))
    print("And the string was " + choice[1])

props = {}
props['FILE'] = "@url:"
props['name'] = ""
props['doubleVal'] = 0.0
props['intVal'] = 0
props['boolVal'] = True
props['vector'] = core.vec3d(1.0, 2.0, 3.0)
props['choice'] = ["Foo", "Bar", "Foo Bar"]

ui.panels.pytools.AddTool("Param Test", props, outputValues, "Test for various parameter types.")
