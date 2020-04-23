# here we are importing a moudle and chaning its name for ease of use
# import my_module as mm
import sys
from my_module import find_index, test
courses = ['history', 'math', 'science', 'art']

index = find_index(courses, 'math')
# print(index)
# print(test)

# we can also import the function from the module as follows and then just use that function rather than having to dot notate. This has been changed above

# we can also import find_index as f or something like that.
# we can also just from my_module import *. this will import all functions from the module. however, this is bad practice becasue we no longer can tell what came from that file.

# when we import a module. it searches a list of directories. here is how we can find that list.

print(sys.path)

# if our import is not in the sys.path, we can add it. by doing sys.path.append('file/location/here')

# change the sys environment to access more locations in windows by going to system properties/ click environment variables and create new environment variable. variable name PYTHON PATH and then the filepath.

# serach Atom pythonpath to find out how to change env in this editor

# The standard library
