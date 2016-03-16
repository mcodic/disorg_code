import os

listdiry = os.listdir("./")

def switching(cc):
	slop = ""
	for ap in cc.lower():
		if ap == " ": 
			ap = "."
		slop = slop + ap
	return slop

formatGood = map(lambda sa:switching(sa), listdiry)
map((lambda tups: os.rename(tups[0], tups[1])), zip(listdiry, formatGood))



# for ee in range(len(listdiry))
# 	os.rename(listdiry[ee], map(switching(), listdiry))

# switchReduce = lambda sdt: reduce((lambda ar,vd: ar+vd), lambda sdt: sdt.lower())

# slop = ""
# lambda wwq: [(lambda tt: slop+=tt) for dd in wwq.lower() if dd == " ": dd="."]

#map((lambda tups: os.rename(tups[0], tups[1])), zip(listdiry, map(lambda sa:switching(sa), listdiry)))