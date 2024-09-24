# python-tests
This repository contains examples of python tools that can be used in FEBioStudio3. Python tools are a way of expanding FEBioStudio's capabilities and implement new, custom features using the powerful Python language. 

## Introduction
This document describes the process of creating python tools for FEBioStudio3. 
Creating a tool is as simple as loading a python script, however, to use the full functionality, it is necessary to embed meta information in the python script. The following sections describe the details. 

## script preamble
To integrate the python script as a tool, FEBioStudio looks for a preamble in the python source file, which is a section defined in a python comment block at the top of the file. The preamble is optional, but only by adding this preamble FBS can generate UI elements that correspond to variables in the python file.

The preamble starts with the identifier `@fbs`

```
# @fbs {
# }
```

Inside the curly braces, a json object defines the contents of the preamble. Currenty, the following list of properties can be added. 

* **name** : This defines the name of the tool. If omitted, the name will be extracted from the script's filename. (usually, the filename with the .py suffix removed)
* **info** : A description of the tool that will be displayed at the top of the tool's widget in FEBio Studio.
* **args** : a dictionary of elements that define the parameters of the script, i.e. the values that the user is expected to provide. 

A simple preamble that defines the tool's name and info property follows. The `args` property is discussed below.  
```
# @fbs {
#   "name" : "My first tool",
#   "info" : "This is my first python tool!"
# }
```

## args property
The `args` property is where the real power lies. This property defines a dictionary of the tool's parameters. Each entry consists of a name and value that defines the type and contents of the parameter. For each parameter, a UI element will be created in FEBio Studio that will allow users to enter values for the parameter. The parameter value is defined either via a short syntax or an extended syntax. The short syntax is only supported for string and float parameters. All other parameters require the extended syntax. 

For float and string parameters, the value can be entered immediately following the parameter's name. The provided value is used as the default value for the corresponding UI element. 
```
# @fbs {
#   "args" : {
#       "name" : "",
#       "age"  : 42
#   }
# }
```

For most parameters, the extended syntax needs to be used. This syntax requires that the value of the parameter is defined itself by a dictionary of predefined attributes. The following attributes are supported (and currently required!)

* **type** : defines the type of the parameter. The type will define what values are allowed and what UI element will be chosen to represent the parameter in the UI.
* **value** : this defines the initial value for the parameter.

The following values can be specified for **type**

* **bool** : a boolean parameter that can only take on the values 0 and 1. A checkbox is used to represent this parameter in the UI
* **int** : an integer parameter
* **float** : a floating point value (double precision variables are used to store the value)
* **string** : a string parameter
* **url** : a string parameter that is interpreted as a url. The UI element will allow users to select a file from the system.
* **enum** : a parameter that can only take on discrete values. The value attribute lists the possible values. A dropdown box is used to represent the property. (The initial value will always be the first item in the list.)
* **vec3** : a parameter that represents a 3D vector. 

```
# @fbs {
#   "args" : {
#       "boolVal"  : { "type" = "bool", "value" = 1 },
#       "intVal"   : { "type" = "int", "value" = 42 },
#       "floatVal" : { "type" = "float", "value" = 3.14 },
#       "stringVal": { "type" = "string", "value" = "eureka!" },
#       "urlVal"   : { "type" = "url", "value" = "C:\path\to\top_secret\file.txt" },
#       "enumVal"  : { "type" = "enum", "value" = ["red", "green", "blue"] },
#       "vec3Val"  : { "type" = "vec3", "value" = [0, 1, 2] }
#   }
# }
```

## Accessing `args` in Python
After the users enters the parameter values in the UI, the script can be run. At that point, the values of the parameters need to become accessible from the python script. The parameters can be accessed from the `args` attribute of the `fbs` module. This attribute is defined as a dictionary that contains the parameter names as keys. 

For example, consider the following python code that defines a single string parameter, called `name`. 

```
# @fbs {
#   "args" : {
#       "name"  : ""
#   }
# }

from fbs import args
print(args['name'])
```

The value of the `name` parameter is accessed in python from the `args` dictionary defined as an attribute of the fbs module. 
