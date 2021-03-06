import math
from copy import deepcopy
import random
import pyximport
pyximport.install()
import dfunc
import sys
#stone & stage reading
#data     = two stone
#onedata  = one stone
#twostage = two stage
#onestage = one stage

param = sys.argv

data = dfunc.getdata(param[1]+'.txt') #stage & stone two data
stage = data[0]
dfunc.addone(stage)
del data[0]

#codes
Maincode = []
for i in range(dfunc.LEN_N):
	Maincode.append(dfunc.maincode(len(data)))

go = 1
ranktable = []
cou = 1
while(cou==1 or ranktable[0][1] > dfunc.TARGET):
	dfunc.crossing(Maincode)
	dfunc.mutation(Maincode)
	allzero = dfunc.check_stop(stage,data,Maincode,ranktable)
	dfunc.sortalive(ranktable)
	result = dfunc.work2(stage,data,Maincode[ranktable[0][0]])
	dfunc.writedata(param[1]+'answer.txt',result)
	Maincode = dfunc.roulette(Maincode,ranktable,allzero)
	cou += 1
