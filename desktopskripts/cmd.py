import sys
import os
import re
import operator as o
import string

#### docs ############
# to append to notes.txt use . as first arg followed by lines
# to append to other textfiles in cwd set in first arg
# if thetextfile does not exist don't worry
# delete lines based on numbers
# print with numbers write without
# switch line
# line ops commonalities

#### improvements ####
# other cmd functionalities
# show only txt

#jungle of possible modes, move one logical level up
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
# do i need this    
if sys.argv[1][:3] == '...': 
    modd = 'cmd'
    morecmd = sys.argv[1:]
     
def getlinecount(): #obsolete
    note2 = open(filename, 'r')
    lastline = str(len([True for x in note2.read() if x == '\n']))
    lastline = '0' + lastline if int(lastline) < 10 else lastline
    note2.close()
    return lastline + " "

# maybe i could have used this method for all line ops
if modd == 'txtfilecmd':  

    note2 = open(filename, 'r+')   
    lineslist = [x for x in note2.readlines()]
    

    if sys.argv[2] == '...del':
        linestodel = list(set(sys.argv[3:]))
        intlintodel = map(int, linestodel)
        intlintodel.sort()
        intlintodel.reverse()
        for dels in intlintodel:
            lineslist.pop(dels)

    if sys.argv[2] == '...switch':    
        linestoinsert = sys.argv[4:len(sys.argv):2]
        indexforinsert = sys.argv[3:len(sys.argv):2]
        intindexs = map(int, indexforinsert)
        for be in intindexs:
            lineslist[be] = '\n'
        map(lineslist.insert, intindexs, linestoinsert)

    if sys.argv[2] == '...print':       
        # new numbering
        j=0
        for brum in lineslist:
            if j < 10:
                print string.strip('0' + str(j) + " " + brum)
            else:    
                print string.strip(str(j) + " " + brum)
            
            j = j + 1



    slicedtext = ''.join(lineslist)
    note2 = open(filename, 'w+')         
    note2.write(slicedtext)
    note2.close()



if modd == 'texxt':
    if filename not in os.listdir(os.getcwd()):
        a = open(filename, 'w+')
        a.write('')
        a.close()


#----------------------------------------------------
def appendlines(argy):
    try:
        note = open(filename, 'a')
        note.write(argy + "\n")
        note.close()
        print 'all good: ' + argy                                           
    except: 
        print '!!! Check your arguments.'
#                   --------------
if modd == 'io':
    if len(morelines) == 1: appendlines(morelines[0])
    else:
          i = 0
          for xs in morelines: 
              appendlines(morelines[i])
              i = i + 1
#----------------------------------------------------------------

if sys.argv[1] == '...rspace':
    formatGood = map(lambda sa: sa.lower().replace(sys.argv[2], sys.argv[3]), os.listdir( "./" ))
    map( (lambda oldy, newy: os.rename( oldy, newy )), os.listdir( "./" ), formatGood )

# add dir view one of the listed and ..
if sys.argv[1] == '...dir':
    
    if len(sys.argv) == 2: 
       dirtarget = "./"
    
    else: 
        if len(sys.argv) > 2: 

            if sys.argv[2] == "..":
               dirtarget = "../"
           
            elif sys.argv[2] in os.listdir("./"):
               dirtarget = "./" + sys.argv[2]
   
    ff = {'directories':[]}
    print '-'*55 + '\n'
    for az in os.listdir(dirtarget):
        if len(az) > 4 and "." in az:
            if az[-4] == '.':
                if az[-3:] not in ff.keys():
                    ff[az[-3:]] = [zx for zx in os.listdir(dirtarget) if zx[-3:] == az[-3:]]
        else: ff['directories'].append(az)


# print this all very nicely
    for dum in ff.keys():
        print dum + "(" + str(len(ff[dum])) + ")"+ ":"
        for mud in ff[dum]:
            print string.rjust(mud, 55)
    print "\ncwd is    " + os.getcwd()            
    print "The total is: " + str(sum([len(ff[kk]) for kk in ff.keys()]))

