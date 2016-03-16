import sys
import os
import re
import operator as o

#### docs ############
# to append to notes.txt use . as first arg followed by lines
# to append to other textfiles in cwd set in first arg
# if thetextfile does not exist don't worry

#### improvements ####
# delete lines based on numbers
# other cmd functionalities

# ...show txt
# ...show jpg
modd = 'empty'
if sys.argv[1][-4:] == '.txt' or sys.argv[1] == '.':
    modd = 'texxt'
    filename = 'notes.txt' if sys.argv[1] == '.' else sys.argv[1]
if modd == 'texxt' and sys.argv[2][:3] != '...':
    modd = 'io'
    morelines = sys.argv[2:]
if modd == 'texxt' and sys.argv[2][:3] == '...':
    modd = 'txtfilecmd'
    moretxtcmd = sys.argv[2:]
if sys.argv[1][:3] == '...': # do i need this
    modd = 'cmd'
    morecmd = sys.argv[1:]
     

if modd == 'txtfilecmd':  
    if sys.argv[2] == '...del':
        note2 = open(filename, 'r+')   
        lineslist = [x for x in note2.readlines()]
        linestodel = list(set(sys.argv[3:]))
        for dels in linestodel:
            lineslist[int(dels)] = ''
        slicedtext = ''.join(lineslist)
        note2 = open(filename, 'w+')         
        note2.write(slicedtext)
        note2.close()

if modd == 'texxt':
    if filename not in os.listdir(os.getcwd()):
        a = open(filename, 'w+')
        a.write('')
        a.close()

def getlinecount():
    note2 = open(filename, 'r')
    lastline = str(len([True for x in note2.read() if x == '\n']))
    lastline = '0' + lastline if int(lastline) < 10 else lastline
    note2.close()
    return lastline + " "

def appendlines(argy):
    try:
        note = open(filename, 'a')
        note.write(getlinecount() + argy + "\n")
        note.close()
        print 'all good: ' + argy										    
    except: 
        print '!!! Check your arguments.'

if modd == 'io':
    if len(morelines) == 1: appendlines(morelines[0])
    else:
          i = 0
          for xs in morelines: 
              appendlines(morelines[i])
              i = i + 1



if sys.argv[1] == '...rspace':
    froms = sys.argv[2]
    tos = sys.argv[3]
    formatGood = map( lambda sa: sa.lower().replace(froms, tos), os.listdir( "./" ) )
    map( (lambda oldy, newy: os.rename( oldy, newy )), os.listdir( "./" ), formatGood )



