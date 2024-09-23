# @fbs {
#  "name" : "Param Test",
#  "info" : "Test for various parameter types",
#  "args" : {
#    "FILE" : { "type" : "url", "value" : ""},
#    "name" : "",
#    "DOUBLEVAL" : 0.1,
#    "int val" : { "type" : "int", "value" : 0 },
#    "boolParam" : { "type" : "bool", "value" : 1 },
#    "vector" : { "type" : "vec3", "value" : [1,2,3] },
#    "choice" : { "type" : "enum", "value" : ["Foo","Bar","Foo bar"] }
#  }
# }
from fbs import ui, args

# grab the arguments from FEBioStudio
FILE = args['FILE']
name = args['name']
DOUBLEVAL = args['DOUBLEVAL']
int_val = args["int val"]
boolParam = args['boolParam']
vector = args["vector"]
choice = args["choice"]

# output the values
print("Checkbox checked: " + str(boolParam))
print("Integer value: " + str(int_val))
print("Double value: " + str(DOUBLEVAL))
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
