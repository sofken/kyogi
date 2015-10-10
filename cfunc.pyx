import math
from copy import deepcopy
import random
import numpy as np
from numba import double
from numba.decorators import jit

#@jit
def Match_rate(list1,list2):
	#import math
	list1_len=len(list1)
	list2_len=len(list2)
	if list1_len<>list2_len:
		return -1
	i=0
	inner=0
	nplist1 = np.array([list1],np.float)
	nplist2 = np.array([list2],np.float)
	nplist12 = np.array(list1,np.float)
	nplist22 = np.array(list2,np.float)
	list1_size = np.linalg.norm(nplist1)
	list2_size = np.linalg.norm(nplist2)
	inner=np.dot(nplist12,nplist22)
	return inner/(math.sqrt(list1_size)*math.sqrt(list2_size))

#IF_stage=[[first],[second],,,]]
#IF_stone=[[first],[second],,,]]
#Main_code=[[first],[second],,,]]
#Trimming_stage=[trimming stage vector]
#stone_now=[now stone vector]

Match_break = 0.8

#@jit
def test(IF_stage,IF_stone,Main_code,Trimming_stage,stone_now):
	IF_stage_number=len(IF_stage)
	IF_stone_number=len(IF_stone)
	#print(Main_code)
	Main_code_number=len(Main_code)
	Match_rate_stone_max=0 #the most semelar in stone(0-1)
	Match_rate_stone_number=-1 #the most semelar in stone index
	Match_rate_stage_max=0
	Match_rate_stage_number=-1
	now_Match_rate=0 #now sone(0-1)
	i=0
	while i<IF_stone_number:
		now_Match_rate=Match_rate(stone_now,(IF_stone[i]))
		if now_Match_rate>Match_rate_stone_max: #rewrite semelar
			Match_rate_stone_number=i
			Match_rate_stone_max=now_Match_rate
		if now_Match_rate>Match_break:
			break
		i+=1
	i=0
	while i<IF_stage_number:
		now_Match_rate=Match_rate(Trimming_stage,IF_stage[i])
		if now_Match_rate>Match_rate_stage_max:
			Match_rate_stage_number=i
			Match_rate_stage_max=now_Match_rate
		if now_Match_rate>Match_break:
			break
		i+=1
	i=0
	Match_rate_stone_ma = round(Match_rate_stone_max,1)
	Match_rate_stone_ma = round(Match_rate_stage_max,1)
	while i<Main_code_number:
		if Main_code[i][0]==Match_rate_stone_number and Main_code[i][1]==Match_rate_stage_number:
			return Main_code[i][2]
		i+=1
	return -1

#get stage & stone data 0->stage 1~->stone
#@jit
def getdata():
	f = open('sample.txt','r')
	tmpdata = []
	data = []
	
	for line in f:
		if(len(line)==2):
			data.append(tmpdata)
			tmpdata = []
		elif(len(line)!=4):
			line = line.rstrip('\r\n')
			tmpdata.append(list(line))
	return data	

#two data -> one data
#@jit
def getone(two):
	twolen = len(two)
	cptwo = deepcopy(two)
	cdef int i
	for i in xrange(twolen-1):
		cptwo[0].extend(cptwo[i+1])
	return cptwo[0]

#@jit
def Count_0(list1):
	cdef int Count=0
	i=0
	for i in list1:
		for j in i:
			if j=='0':
				Count+=1
	return Count

#put stone
#@jit
def putstone(stage,stone,coor,dire,act):
	#coor(coordinate)...(X,Y)
	#dire(direction)...1(up) 2(bottom) 3(left) 4(right)

	cdef int i
	cdef int j
	cdef int k
	cdef int l
	#operate against stone
	if(act[1]!=7):
		cpstone = roll(stone,act[1])
		if(act[2] == 1):
			cpstone = lrchange(cpstone)
		cpact = findone(cpstone,act[0][0],act[0][1])
	
		#put
		if(dire == 1):
			zerox = coor[0]-cpact[0]
			zeroy = coor[1]-cpact[1]-1
		elif(dire == 2):	
			zerox = coor[0]-cpact[0]
			zeroy = coor[1]-cpact[1]+1
		elif(dire == 3):
			zerox = coor[0]-cpact[0]-1
			zeroy = coor[1]-cpact[1]
		elif(dire == 4):
			zerox = coor[0]-cpact[0]+1
			zeroy = coor[1]-cpact[1]
	
		passes = 1
		for i in xrange(8):
			for j in xrange(8):
				if(stage[i+zeroy][j+zerox]=='0' and cpstone[i][j]=='1'):
						stage[i+zeroy][j+zerox] = '3'
				elif((stage[i+zeroy][j+zerox]=='1' or stage[i+zeroy][j+zerox]=='2') and cpstone[i][j]=='1'):
					passes = 0
					break
	
		HT=['H','T']
		#3->2 or 3->1
		if(passes == 1):
			change = '2'
			#print(zerox,zeroy,HT[act[2]],act[1]*90)
		else:
			change = '0'
			#print(' ')
		for k in xrange(8):
			for l in xrange(8):
				if(stage[k+zeroy][l+zerox]=='3'):
					stage[k+zeroy][l+zerox] = change
		return passes
	else:
		#print(' ')
		return 0

def putstone_2(stage,stone,coor,dire,act):
	#coor(coordinate)...(X,Y)
	#dire(direction)...1(up) 2(bottom) 3(left) 4(right)

	cdef int i
	cdef int j
	cdef int k
	cdef int l
	#operate against stone
	if(act[1]!=7):
		cpstone = roll(stone,act[1])
		if(act[2] == 1):
			cpstone = lrchange(cpstone)
		cpact = findone(cpstone,act[0][0],act[0][1])
	
		#put
		if(dire == 1):
			zerox = coor[0]-cpact[0]
			zeroy = coor[1]-cpact[1]-1
		elif(dire == 2):	
			zerox = coor[0]-cpact[0]
			zeroy = coor[1]-cpact[1]+1
		elif(dire == 3):
			zerox = coor[0]-cpact[0]-1
			zeroy = coor[1]-cpact[1]
		elif(dire == 4):
			zerox = coor[0]-cpact[0]+1
			zeroy = coor[1]-cpact[1]
	
		passes = 1
		for i in xrange(8):
			for j in xrange(8):
				if(stage[i+zeroy][j+zerox]=='0' and cpstone[i][j]=='1'):
						stage[i+zeroy][j+zerox] = '3'
				elif((stage[i+zeroy][j+zerox]=='1' or stage[i+zeroy][j+zerox]=='2') and cpstone[i][j]=='1'):
					passes = 0
					break
	
		HT=['H','T']
		#3->2 or 3->1
		if(passes == 1):
			change = '2'
			result = str(zerox)+','+str(zeroy)+','+HT[act[2]]+','+str(act[1]*90)
			print(result)
		else:
			change = '0'
			print('')
		for k in xrange(8):
			for l in xrange(8):
				if(stage[k+zeroy][l+zerox]=='3'):
					stage[k+zeroy][l+zerox] = change
		return passes
	else:
		print('')
		return 0

#roll vector
#@jit
def roll(stone,times):
	rollstone = []
	putzero(rollstone,8)
	#rollstone = deepcopy(stone)
	#copystone = deepcopy(stone)
	cdef int k
	cdef int i
	cdef int j
	if(times == 0):
		times = 4
	for k in xrange(times):
		for i in xrange(8):
			for j in xrange(8):
				nexti = j
				nextj = 7-i
				rollstone[nexti][nextj] = stone[i][j]
		#copystone = deepcopy(rollstone)
	return rollstone

#change left and right
#@jit
def lrchange(stone):
	changestone = []
	putzero(changestone,8)
	#changestone = deepcopy(stone)
	cdef int i
	cdef int j
	for i in xrange(8):
		for j in xrange(8):
			nextj = 7 - j
			changestone[i][nextj] = stone[i][j]
	return changestone

#add many 1
#@jit
def addone(stage):
	cdef int i
	cdef int j
	cdef int k
	cdef int l
	for i in xrange(32):
		for j in xrange(10):
			stage[i].append('1')
	for k in xrange(10):
		stage.append([])
		for l in xrange(42):
			stage[k+32].append('1')

#find 1 in stone
#@jit
def findone(stone,x,y):
	cdef int i
	cdef int j
	cdef int k
	for i in xrange(8):
		for j in xrange(i+1):
			for k in xrange(i+1):
				if(j+y<8 and k+x<8 and stone[j+y][k+x]=='1'):
					one = [k+x,j+y]
					return one
				elif(y-j>-1 and x-k>-1 and stone[y-j][x-k] == '1'):
					one = [x-k,y-j]
					return one
				elif(y-j>-1 and k+x<8 and stone[y-j][k+x]=='1'):
					one = [k+x,y-j]
					return one
				elif(j+y<8 and x-k>-1 and stone[j+y][x-k] == '1'):
					one = [x-k,j+y]
					return one

#@jit
def Find_side(STAGE):
	n=32
	Side=[]
	cdef int j
	cdef int i
	for j in xrange(n) :
		for i in xrange(n):
			if STAGE[i][j]=='2' :
				if(STAGE[i-1][j]=='0'):
					Side.append([1,[j,i]])
				if(STAGE[i+1][j]=='0'):
					Side.append([2,[j,i]])
				if(STAGE[i][j-1]=='0'):
					Side.append([3,[j,i]])
				if(STAGE[i][j+1]=='0'):
					Side.append([4,[j,i]])
	return Side

#@jit
def trimming(SIDE,STAGE):
	a=len(SIDE)
	k=0
	t_stage = []
	while k<a :
		SIDE[k][1][0] = SIDE[k][1][0]-4
		SIDE[k][1][1] = SIDE[k][1][1]-4
		B = SIDE[k]
   
		t_stage.append([])
		i=SIDE[k][1][1]

		i1=SIDE[k][1][1]
		j1=SIDE[k][1][0]
		c = 0
		while i<i1+9 :
			j=SIDE[k][1][0]

			while j<j1+9 :
				t_stage[k].append(STAGE[i][j])
				j+=1
				continue

			i+=1
			continue

		k+=1

	return t_stage

#View Stage for DEBUG
#@jit
def viewstage(twostage):
	cdef int i
	cdef int j
	for i in xrange(32):
		line = ""
		for j in xrange(32):
			line += twostage[i][j]
		print(line)

#search first step
#@jit
def putfirst(stage,data,onedata,IF_stage,IF_stone,act,Main_code,n):
	twolist = []
	cdef int i
	cdef int j
	for i in xrange(32):
		for j in xrange(32):
			if(stage[i][j]=='1'):
				if(stage[i-1][j] == '0' or stage[i][j-1] == '0' or stage[i+1][j] == '0' or stage[i][j+1] == '0'):
					stage[i][j] = '2'
					twolist.append([i,j])
	res = putting(stage,data,onedata,IF_stage,IF_stone,act,Main_code,n)
	#viewstage(twostage)
	for k in twolist:
		stage[k[0]][k[1]] = '1'
	return res

def putfirst_2(stage,data,onedata,IF_stage,IF_stone,act,Main_code,n):
	twolist = []
	cdef int i
	cdef int j
	for i in xrange(32):
		for j in xrange(32):
			if(stage[i][j]=='1'):
				if(stage[i-1][j] == '0' or stage[i][j-1] == '0' or stage[i+1][j] == '0' or stage[i][j+1] == '0'):
					stage[i][j] = '2'
					twolist.append([i,j])
	res = putting_2(stage,data,onedata,IF_stage,IF_stone,act,Main_code,n)
	#viewstage(twostage)
	for k in twolist:
		stage[k[0]][k[1]] = '1'
	return res

#@jit
def IF_STAGE():
	if_stage=[]
	k=0
	while k<10 :  #2個つくる
		j=0
		tmp = []
		while j<9*9 :
			tmp.extend(str(random.randint(0,1)))
			j+=1
			continue

		if_stage.append(tmp)

		k+=1

	return if_stage

#@jit
def IF_STONE():
	if_stone=[]
	k=0
	while k<10 :  
		j=0
		tmp = []
		while j<8*8 :
			tmp.extend(str(random.randint(0,1)))
			j+=1
			continue
		if_stone.append(tmp)
		k+=1

	return if_stone

#@jit
def actcode() :
	act=[]
	i=0
	while i<1000 :

		act.append([[random.randint(0,7),random.randint(0,7)],random.randint(0,3),random.randint(0,1)])

		i+=1

	return act

#@jit
def maincode(length):
	main=[]
	cdef int i=0
	while i<length :
		passes = 0
		arnd = random.randint(0,9)
		brnd = random.randint(0,9)
		main.append([arnd,brnd,random.randint(0,999)])
		i+=1
	return main

#@jit
def putting(stage,data,onedata,IF_stage,IF_stone,act,Main_code,n):
	side=Find_side(stage)
	sidelen = len(side)
	tristage = trimming(side,stage)
	res = 0 #0...loop
	cdef int times = 0
	while(res==0 and times<sidelen):
		#random.seed()
		#rnd = random.randint(0,sidelen-1)
		rnd = times-1
		action = test(IF_stage,IF_stone,Main_code,tristage[rnd],onedata[n])
		res = putstone(stage,data[n],[side[rnd][1][0]+4,side[rnd][1][1]+4],side[rnd][0],act[action])
		times += 1
	return res

def putting_2(stage,data,onedata,IF_stage,IF_stone,act,Main_code,n):
	side=Find_side(stage)
	sidelen = len(side)
	tristage = trimming(side,stage)
	res = 0 #0...loop
	cdef int times = 0
	while(res==0 and times<sidelen):
		#random.seed()
		#rnd = random.randint(0,sidelen-1)
		rnd = times-1
		action = test(IF_stage,IF_stone,Main_code,tristage[rnd],onedata[n])
		res = putstone_2(stage,data[n],[side[rnd][1][0]+4,side[rnd][1][1]+4],side[rnd][0],act[action])
		times += 1
	return res

#@jit
def allclear(lista):
	length = len(lista)
	cdef int i
	for i in xrange(length):
		lista.pop()

#Genetic algorithm	
#contents
LEN_N = 5 #Main code len
LEN_B = 9 #After born Main code len
TARGET = 400
DEATH = 4 #not death percentage
PER = 10 #not mutation percentage
MAINLEN = 50

#radian -> x
#@jit
def work(stage,data,onedata,IF_stage,IF_stone,act,Main_code):
	#first
	cdef int i
	cdef int n
	res = 0
	stonelen = len(data)
	while(res==0 and i<stonelen):
		res = putfirst(stage,data,onedata,IF_stage,IF_stone,act,Main_code,i)
		i += 1
	#put stone & output
	
	for n in xrange(stonelen-i):
	#for n in [i]:
		#tromming datas
		putting(stage,data,onedata,IF_stage,IF_stone,act,Main_code,n+i)
		#viewstage(twostage)
	
	zero = Count_0(stage)
	#viewstage(stage)
	return zero
	#viewstage(twostage)
	#random in 0-180

def work_2(stage,data,onedata,IF_stage,IF_stone,act,Main_code):
	#first
	cdef int i = 0
	cdef int n
	res = 0
	stonelen = len(data)
	while(res==0 and i<stonelen):
		res = putfirst_2(stage,data,onedata,IF_stage,IF_stone,act,Main_code,i)
		i += 1
	#put stone & output
	
	for n in xrange(stonelen-i):
	#for n in [i]:
		#tromming datas
		putting_2(stage,data,onedata,IF_stage,IF_stone,act,Main_code,n+i)
		#viewstage(twostage)
	
	zero = Count_0(stage)
	#viewstage(stage)
	return zero
	#viewstage(twostage)
	#random in 0-180

#check stop revoluation
#@jit
def check_stop(lista,ranktable,cpstage,data,onedata,IF_stage,IF_stone,act):
	cdef int go = 1
	cdef int j = 0
	allclear(ranktable)
	#cp2stage = deepcopy(cpstage)
	for i in lista:
		cp2stage = deepcopy(cpstage)
		zero = work(cp2stage,data,onedata,IF_stage,IF_stone,act,i)
		ranktable.append([j,zero])
		if zero <= TARGET: #warning
			go = 0
		j += 1
	return go

def check_stop_2(lista,ranktable,cpstage,data,onedata,IF_stage,IF_stone,act):
	cdef int go = 1
	cdef int j = 0
	allclear(ranktable)
	#cp2stage = deepcopy(cpstage)
	for i in lista:
		cp2stage = deepcopy(cpstage)
		zero = work_2(cp2stage,data,onedata,IF_stage,IF_stone,act,i)
		if zero <= TARGET: #warning
			go = 0
		j += 1
	return go

#Crossing
#@jit
def crossing(lista):
	cdef int i
	cdef int one = 0
	cdef int two = 0
	cdef int rnd1 = 0
	cdef int rnd2 = 0
	cdef int length = 0
	for i in xrange((LEN_B-LEN_N)/2):
		one = 0
		two = 0
		rnd1 = 0
		rnd2 = 0
		length = len(lista[0])
		while one == two:
			one = random.randint(0,LEN_N-1)
			two = random.randint(0,LEN_N-1)
		tmp1 = deepcopy(lista[one])
		tmp2 = deepcopy(lista[two])
		#for j in xrange(1000):
		while rnd1 == rnd2:
			rnd1 = random.randint(0,length/2)
			rnd2 = random.randint(length/2,length-1)
		#tmp1[rnd],tmp2[rnd] = tmp2[rnd],tmp1[rnd]
		#tmp1[rnd+1],tmp2[rnd+1] = tmp2[rnd+1],tmp1[rnd+1]
		#tmp1[rnd+2],tmp2[rnd+2] = tmp2[rnd+2],tmp1[rnd+2]
		tmp1[rnd1:rnd2],tmp2[rnd1:rnd2] = tmp2[rnd1:rnd2],tmp1[rnd1:rnd2]
		lista.append(tmp1)
		lista.append(tmp2)

#sort(aliving)
#@jit
def sortalive(ranktable):
	ranktable.sort(key=lambda rank: rank[1])
	print(ranktable[0])

#death in roulette
#@jit
#def roulette(lista,ranktable):
#	cdef int i = LEN_N
#	cdef int j = 0
#	cdef int rnd
#	random.seed()
#	dellist = []
#	while i>0:
#		rnd = random.randint(0,50)
#		print(rnd,j,i)
#		if(rnd >= (j+1+LEN_N-i)*DEATH):
#			dellist.append(lista[ranktable[j][0]])
#			ranktable.pop(j)
#			j -= 1
#			i -= 1
#		#if(j < LEN_B-LEN_N-1+i):
#		if(j < 50):
#			j += 1
#		else:
#			j = 0
#	l = 0
#	allclear(lista)
#	for k in dellist:
#		lista.append(k)
#	allclear(ranktable)

def roulette(lista,ranktable):
	cdef int i
	cdef int rnd
	cdef int length = len(ranktable)
	alivelist = []
	for i in xrange(LEN_N):
		alivelist.append(lista[ranktable[i][0]])
	allclear(lista)
	lista.extend(alivelist)
	allclear(alivelist)
	return lista

#mutation
#@jit
def mutation(lista):
	cdef int i
	length = len(lista[0])
	cdef int rnd2
	cdef int rnd3
	cdef int rnd4
	for i in xrange(LEN_B-1):
		rnd1 = random.random()*100
		#rnd2 = random.randint(0,LEN_B-1)
		#rnd3 = random.randint(0,length-1)
		#rnd4 = random.randint(0,length-1)
		if(rnd1 <= PER):
			#lista[i][rnd3:rnd4],lista[rnd2][rnd3:rnd4] = lista[rnd2][rnd3:rnd4],lista[i][rnd3:rnd4]
			lista[i+1][0:(MAINLEN/2+1)] = maincode(MAINLEN/2)
	return lista

def putzero(lista,length):
	cdef int i
	cdef int j
	for i in xrange(length):
		lista.append([])
		for j in xrange(length):
			lista[i].append(0)
