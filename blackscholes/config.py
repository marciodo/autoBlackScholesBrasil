import os
import yaml

# Get the name of init file from yaml init document
initFile = os.path.dirname(__file__)
initFile += '/blackscholes_init.yaml'
stream = file(initFile, 'r')
initData = yaml.load(stream)

# Get db filename
dbFilename = initData['dbFilename']
