"""
use it when there are no folders
or just copy the files into separate folder, run and return
this is the only usable implementation
"""

import mcodic.doug as doug
import mcodic.fs as fsys
import os


fileList = doug.jsonFileData("./cwdFiles.json")

for folderName in map(fsys.rext, fileList):
     os.mkdir(folderName)


