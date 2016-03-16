import os
import sys
import operator as o
import re

def dotdelim( cc ):
    slop = ""

    for ap in cc .lower( ):

        if  o.eq( ap, " " ) : ap =  "."

        slop = slop + ap

    return slop
# '.'.join(cc.lower().split(' '))
# re.sub('\W','.', cc).lower()


# def spacetodot( text ):
# 	"""\
# 	THEFUNCTIONTAKESASTRINGANDRETURNSASTRINGLIST
# 	CHANGESALLCHARTOLOWERCASEANDWHITESPACESTODOTS
# 	"""

# 	return map( lambda sa: dotdelim( sa ), text )
	

def ftfilter( ext ):
	"""\
	THEFUNCTIONTAKESASTRINGANDRETURNSNONE
	PRINTSALLFILESWITHARGEXTENSIONINCWD
	"""
	infolder = os.listdir( os.getcwd() )
	extfilter = filter( (lambda x: o.eq( x[-4:], "." + ext )), infolder )
	print "all ." + ext + " files:\n"
	map( (lambda nline: sys.stdout.write( o.concat( nline, "\n" ) ))
		, extfilter )


def charli( dq ): 
    '''\
    TAKESASTRINGANDRETURNSASTRINGLIST
    USEDINSTRINGPOPFUNCTION
    '''
    return map( lambda wa: wa, dq )
    # list(dq)


def joincharli( listy ):
    '''\
    TAKESALISTOFSTRINGSANDRETURNSASTRING
    USEDINSTRINGPOPFUNCTION
    '''
    ahandle = listy

    ahandle .insert( 0, "" )

    return reduce( (lambda a, d: o.concat( a, d )), ahandle )
# ''.join(listy)

def stringpop( stringy, pos = None ):
    '''\
    TAKESASTRINGANDOPTIONALYANDINTANDRETURNSASTRING
    STRINGSAREIMMUTABLEBUTITCANBEUSEDASVALUES
    '''
    listhandle = charli( stringy )

    if pos == None : listhandle .pop( )
    else:            listhandle .pop( pos )
    
    return joincharli( listhandle )







def oddlist(inplist):
    retlist = []
    for i in range(len(inplist)+1)[1:]:
        if i % 2 != 0:
            retlist.append(inplist[i-1])
    return retlist

def evenlist(inplist):
    retlist = []
    for i in range(len(inplist)+1)[1:]:
        if i % 2 == 0:
            retlist.append(inplist[i-1])
    return retlist





def listinpairs(linearlist):
    """ 
    [a] -> [t]
    Turnes a list into list of linear pairs 
    """
    ddo = oddlist(linearlist)
    neve = evenlist(linearlist)
    return map((lambda ew,qa:(ew,qa)), ddo, neve)



def listindoubles(linearlist):
    """ 
    [a] -> [t]
    Turnes a list into list of list doubles 
    """
    ddo = oddlist(linearlist)
    neve = evenlist(linearlist)
    return map((lambda ew,qa:[ew,qa]), ddo, neve)


def rmdupli(az): 
    """
    [a] -> [a]
    """
    return list(set(az))

def numtocharli(nmb):
    """
    n -> [c]
    """
    return list(str(nmb))

def intwordy(intara):
    zil = numtocharli(intara)
    br = len(zil)
    #12 344 654 452 4 3 3