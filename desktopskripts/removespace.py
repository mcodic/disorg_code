import os
import operator as o

formatGood = map( lambda sa: sa.lower().replace(' ', ''), os.listdir( "./" ) )
map( (lambda oldy, newy: os.rename( oldy, newy )), os.listdir( "./" ), formatGood )
print "\n\n   White space removed."

#def switching( cc ): 
    # slop = ""
    # for ap in cc .lower( ) :
    #   if  o.eq( ap, " " ) : ap =  "."
    #   slop = slop + ap
    # return slop

#listdiry = os.listdir( "./" )
#formatGood = map( lambda sa: switching( sa ), os.listdir( "./" ) )
# map( (lambda tups: os.rename( tups[0], tups[1] ))
#   , zip( listdiry, formatGood ) )




