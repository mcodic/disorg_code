# SAVEDASUTF8WITHBOM

import             string
import operator as o
import             sys
import             os

# USERINTERACTION

if o .eq( len( sys .argv ), 1 ): 

	infolder  = os .listdir( os .getcwd( ) )
	txtfilter = filter( (lambda x: o .eq( x[-4:], ".txt" )), infolder )

	print "all .txt files:" "\n" 
	map(  (lambda nline: sys .stdout .write( o .concat( nline, "\n" ) )) 
		 , txtfilter )

	print "\ninput string of filename that you want to convert:"
	ime      = input( )
	someFile = open( ime )

else:
	ime      = None
	someFile = open( sys .argv[1] )
	print o .concat( 'Your filename is ', sys .argv[1] )

print len( sys .argv )
if len( sys .argv ) < 3  or o.ne(sys .argv[2], ("print" or 'write')): 

    print "'print' or 'write'?"
    adsd   = input( )

else: adsd   = sys .argv[2]


# MEAT

set      = o .concat( string .uppercase, string .digits )
superSet = o .concat( set             , string .whitespace )

ddd = filter( (lambda x: o .and_( o. contains( superSet, x ), o .ne( x, " " ) ))
	         , someFile .read( ) .upper() )


# OUTPUTCHOISES

if   adsd == 'print':
              print ddd

elif adsd ==          'write':

    if ime == None: imeNoExt = sys .argv[1] 

    else:           imeNoExt = ime[:-4]

    outputWriteUpper = open( o .concat( imeNoExt .upper( ), "UPPER.enm" ), "w" )
    outputWriteUpper  .write( ddd )
    outputWriteUpper  .close( )

else:         print "haven't decided?"
	

someFile              .close( )