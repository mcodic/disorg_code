"""
make a json file with a 
list of all files in cwd
"""
import json
import os

fileList = os.listdir(os.getcwd())
jsonFile = open("cwdFiles.json", "w+")
jsonFile.write(json.dumps(fileList, indent=2))
jsonFile.close()