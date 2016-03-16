import string
import operator as oper
import sys

set=oper.concat(string.uppercase,string.digits)
superSet=oper.concat(set,string.whitespace)
print "input string of filename that you want to convert:"
ime=input()

someFile=open(ime)

print "'print' or 'write'?"

ddd =filter((lambda x: x in superSet and x!=" "), someFile.read().upper())

adsd=input()

if adsd == 'print':
	print ddd
elif adsd == 'write': 
	imeNoExt = ime[:-4]
	outputWriteUpper=open(oper.concat(imeNoExt.upper(),"UPPER.enm"),"w")
	outputWriteUpper.write(ddd)
	outputWriteUpper.close()
else: print "haven't decided?"
	
someFile.close()