"""
get this module with  import mcodic.doug as doug
for dealing with json data directly
"""
_all_ = ["jsonFileData"]

import json   # for getting the data

def jsonFileData(address):
    """
    path -> python data
    take data from external json file and return stuff in python
    """
    a = open(address)
    b = a.read()
    a.close()
    return json.loads(b)