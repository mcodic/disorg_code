import os
import re

#### PROGRAM IMPROVEMENTS ####
##############################
# format the output by re.ext, add date etc. izbaci emptylines
# add a console response all good
# add some data number of folders, number of files

#### DOCUMENTATION ###########
##############################

subfolders = os.listdir( os.getcwd() )

fileList   = open( "dirlist.txt", "w+" )

map( lambda strip: fileList.write( strip + "\r" ), subfolders )

fileList.close()