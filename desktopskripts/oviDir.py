import os

subfolders = os.listdir( os.getcwd() )

fileList   = open( "subdirlist.txt", "w+" ) 

map( lambda strip: fileList.write( strip + "\r\n" ), subfolders )

fileList.close()