# python-tests
This repository contains examples of python tools that can be used in FEBioStudio3. Python tools are a way of expanding FEBioStudio's capabilities and implement new, custom features using the powerful Python language. 

## Introduction
This document describes the process of creating python tools for FEBioStudio3. 
At the start of the script, import the **fbs** module to gain access to the FEBio Studio Python interface.

```
from fbs import *
```

A script containing a python tool will need to do three things: 
1. Define the function that contains the logic of the tool. This function will be called from FBS.
2. Define a dictionary containing the properties of the tool. 
3. Add the tool to the UI.
The following sections describe this process in more details.

## Creating the Tool

### Define a python function
The logic of the tool should be coded in a Python function. Please note that the name given to the parameters (if any) must match the names defined in the dictionary that defines the tool's properties, as detailed below. 
The Python script can contain multiple functions (or other Python objects), but only one function can execute the tool's logic.

### Define the tool's properties
A tool's properties are specified in a Python dictionary. The entries in the dictionary are key-value pairs. The key defines the property name (and must match the parameter names of the Python function), and the value sets the initial value of the corresponding property. The implied type of this initial value will define the UI widget that will be assigned to the property. 

For example, this code extract shows how to create different properties.

```
props = {} # start with an empty dictionary
props['name'   ] = "John Doe"  # creates a string property
props['age'    ] = 39          # creates an int property
props['income' ] = 45000.0     # creates a float property
props['married'] = True        # creates a bool property
props['file'   ] = "@url:C:/home/folder/data.txt"   # creates a resource property. The initial value is set to "C:/home/folder/data.txt"
props['enums'  ] = ["Option1", "Option2", "Option3"] # creates an enum property.  
```

Note that in order to differentiate between a string input field and a url input file, start the initial value with "@url:" (The colon is required). The input widget will then offer users a way to select a file using a standard file open dialog. 

To define enum properties, set the value to a list of strings. The input widget will show a combo box that lists the specified strings as options.

The properties should be defined in the same order as the function arguments. The types of the function arguments will be the same as the corresponding types of the properties, except for enum properties. For enum properties, the parameter that will be passed to the function is a tuple that has two elements. The first element is an int that contains the zero-based index into the options list. The second element is the corresponding string of the option. 

```
# to define an enum, specify the string values as a list
props['enums'  ] = ["Option1", "Option2", "Option3"] # creates an enum property.

# in the function, this argument will be passed as a tuple
def f(enums):
    optionIndex  = enums[0]    # contains the zero-based index into the options list
    optionString = enums[1]    # contains the string value of the corresponding option
```

### Add the tool to the UI

To add the tool to the UI, use the **fbs.ui.panels.pytools.AddTool** function. This function requires four parameters.

* **name**  : Specifies the name of the tool. 
* **props** : The dictionary containing the tool's properties
* **func**  : The python function that will be called by FBS. 
* **info**  : (optional) A description of the tool. 

For example:
(Assume props is a dictionary, and myTool a function)
```
ui.panels.pytools.AddTool("My Tool", props, myTool, "My first tool")
```

## An example
This example doesn't do anything useful but simply demonstrates a complete example of a python tool. 

```
# import the fbs modules
from fbs import *

# this is the function we'll call
def myFunction(name, age):
    print(f"{name} is {age} years old")

# the properties
p = {}
p['name'] = "John Doe"
p['age'] = 39

# add it to the UI
ui.panels.pytools.AddTool("My Tool", p, myFunction)

```
