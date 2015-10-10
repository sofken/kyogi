import math
from copy import deepcopy
import random
import numpy as np
from numba import double
from numba.decorators import jit
import pyximport
pyximport.install()
import cfunc

#stone & stage reading
#data     = two stone
#onedata  = one stone
#twostage = two stage
#onestage = one stage

data = cfunc.getdata() #stage & stone two data
onedata = []
for i in range(len(data)):
	onedata.append(cfunc.getone(data[i])) #stage & stone one data
twostage = data[0]

cfunc.addone(twostage)

del data[0]
onestage = onedata[0]
del onedata[0]

#codes
IF_stage = cfunc.IF_STAGE()
IF_stone = cfunc.IF_STONE()
act = cfunc.actcode()
act.append([[7,7],7,7])
Main_code = []
LEN_N = 5
MAINLEN = 50
for i in range(LEN_N):
	Main_code.append(cfunc.maincode(MAINLEN))

cpstage = deepcopy(twostage)

go= 1

ranktable = []
cou = 1
while(go):
	cfunc.crossing(Main_code)
	cfunc.mutation(Main_code)
	go = cfunc.check_stop(Main_code,ranktable,cpstage,data,onedata,IF_stage,IF_stone,act)
	cfunc.sortalive(ranktable)
	if(go == 0):
		#cfunc.check_stop_2([Main_code[ranktable[0][0]]],ranktable,cpstage,data,onedata,IF_stage,IF_stone,act)
		break

	#cfunc.work_2(cpstage,data,onedata,IF_stage,IF_stone,act,Main_code[ranktable[0][0]])
	cfunc.roulette(Main_code,ranktable)
	cou += 1
	#go = check_stop(Main_code,ranktable,cpstage,data,IF_stage,IF_stone,act)
	#viewstage(cpstage)
#result = [Main_code[ranktable[0][0]]]
#cfunc.check_stop_2(result,ranktable,cpstage,data,onedata,IF_stage,IF_stone,act)
