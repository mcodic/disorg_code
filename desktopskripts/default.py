
# this is a boilerplate dbz

import os
import shutil
import json   # for getting the data
import inspect

# maybe some functions that prefills the text files
# titles, ------, and so on



def jsonFileData(address):
    a = open(address)
    b = a.read()
    a.close()
    return json.loads(b)


print(jsonFileData("./default.json")["txtFileList"])


input()
folderList = []

