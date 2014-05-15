import sys, os


path = raw_input('The path to the module you wish to import: ')
e = os.path.exists(path)
module = ''
while(not(e)):
    path = raw_input('Try again! Provide the path to the module you wish to import: ')
    e = os.path.exists(path) and os.path.isfile(path)
    if (e):
        module = os.path.split(path)[1]
        module = module.split('.py')[0] #Remove the .py module extension
        e = e and module
        path = os.path.split(path)[0]

sys.path.append(path)
exec 'from ' + module + ' import *'

#TODO: add error handling for beginner users
