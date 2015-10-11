import math
from copy import deepcopy
import random

#get stage & stone data 0->stage 1~->stone
def getdata(filename):
	f = open(filename,'r')
	tmpdata = []
	data = []
	
	for line in f:
		if(len(line)==2):
			data.append(tmpdata)
			tmpdata = []
		elif(len(line)!=4 and len(line)!=5):
			line = line.rstrip('\r\n')
			tmpdata.append(list(line))
	data.append(tmpdata)
	f.close()
	return data	

def writedata(filename,str):
	f = open(filename,'w')
	f.write(str)
	f.close()

def Count_0(list1):
	cdef int Count=0
	i=0
	for i in list1:
		for j in i:
			if j=='0':
				Count+=1
	return Count

def putfirst(stage,stone,x,y):
	#HT=['H','T']
	cdef int passes = 1
	cdef int i
	cdef int j
	cdef int k
	cdef int l
	for i in xrange(8):
		for j in xrange(8):
			if(stage[i+y][j+x]=='0' and stone[i][j]=='1'):
					stage[i+y][j+x] = '3'
			elif((stage[i+y][j+x]=='1' or stage[i+y][j+x]=='2') and stone[i][j]=='1'):
				passes = 0
				break
		if(passes==0):
			break
	
	#3->2 or 3->1
	if(passes==1):
		change = '2'
	elif(passes==0):
		change = '0'
	for k in xrange(8):
		for l in xrange(8):
			if(stage[k+y][l+x]=='3'):
				stage[k+y][l+x] = change
	return passes

#put stone
def putstone(stage,stone,x,y):
	#HT=['H','T']
	cdef int passes = 2
	cdef int i
	cdef int j
	cdef int k
	cdef int l
	for i in xrange(8):
		for j in xrange(8):
			if(stage[i+y][j+x]=='0' and stone[i][j]=='1'):
					stage[i+y][j+x] = '3'
			elif((stage[i+y][j+x]=='1' or stage[i+y][j+x]=='2') and stone[i][j]=='1'):
				passes = 0
				break
			if((stage[i+y+1][j+x]=='2' or stage[i+y-1][j+x]=='2' or stage[i+y][j+x+1]=='2' or stage[i+y][j+x-1]=='2') and stone[i][j]=='1'):
				passes = 1
		if(passes==0):
			break
	
	#3->2 or 3->1
	if(passes==1):
		change = '2'
	elif(passes==0 or passes==2):
		change = '0'
	for k in xrange(8):
		for l in xrange(8):
			if(stage[k+y][l+x]=='3'):
				stage[k+y][l+x] = change
	return passes

#roll vector
def roll(stone,times):
	rollstone = []
	putzero(rollstone,8)
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
	return rollstone

#change left and right
def lrchange(stone,change):
	changestone = []
	putzero(changestone,8)
	cdef int i
	cdef int j
	for i in xrange(8):
		for j in xrange(8):
			if(change == 1):
				nextj = 7 - j
			else:
				nextj = j
			changestone[i][nextj] = stone[i][j]
	return changestone

#add many 1
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

#View Stage for DEBUG
def viewstage(twostage):
	cdef int i
	cdef int j
	for i in xrange(32):
		line = ""
		for j in xrange(32):
			line += twostage[i][j]
		print(line)

def maincode(length):
	main=[]
	cdef int i
	cdef int x
	cdef int y
	cdef int lr
	cdef int roll
	for i in range(length):
		x = random.randint(0,33)
		y = random.randint(0,33)
		lr = random.randint(0,1)
		roll = random.randint(0,3)
		main.append([x,y,lr,roll])
	return main

def allclear(lista):
	length = len(lista)
	cdef int i
	for i in xrange(length):
		lista.pop()

#Genetic algorithm	
#contents
LEN_N = 200 #Main code len
LEN_B = 440 #After born Main code len
TARGET = 50
PER = 20 #not mutation percentage

def work(stage,stones,maincode):
	cdef int zero
	cdef int first = 0
	cdef int i = 0
	for main in maincode:
		cpstone = lrchange(stones[i],main[2])
		cpstone = roll(cpstone,main[3])
		if(first == 0):
			first = putfirst(stage,cpstone,main[0],main[1])
		else:
			putstone(stage,cpstone,main[0],main[1])
		i += 1
	zero = Count_0(stage) 
	return zero

def work2(stage,stones,maincode):
	HT = ['H','T']
	cdef int zero
	cdef int first = 0
	cdef int i = 0
	result = ''
	cpstage = deepcopy(stage)
	for main in maincode:
		cpstone = lrchange(stones[i],main[2])
		cpstone = roll(cpstone,main[3])
		if(first == 0):
			first = putfirst(cpstage,cpstone,main[0],main[1])
			if(first==1):
				result += str(maincode[i][0])+' '+str(maincode[i][1])+' '+HT[maincode[i][2]]+' '+str(maincode[i][3]*90)+'\n'
			else:
				result += '\n'
		else:
			res = putstone(cpstage,cpstone,main[0],main[1])
			if(res==1):
				result += str(maincode[i][0])+' '+str(maincode[i][1])+' '+HT[maincode[i][2]]+' '+str(maincode[i][3]*90)+'\n'
			else:
				result += '\n'
		i += 1
	return result

def check_stop(stage,stones,maincodes,ranktable):
	cdef int i = 0
	cdef int zero
	cdef int allzero
	allclear(ranktable)
	allzero = 0
	for maincode in maincodes:
		cpstage = deepcopy(stage)
		zero = work(cpstage,stones,maincode)
		ranktable.append([i,zero])
		i += 1
		allzero += zero
	return allzero

def crossing(maincodes):
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
		length = len(maincodes[0])
		while one == two:
			one = random.randint(0,LEN_N-1)
			two = random.randint(0,LEN_N-1)
		tmp1 = deepcopy(maincodes[one])
		tmp2 = deepcopy(maincodes[two])
		while rnd1 == rnd2:
			rnd1 = random.randint(0,length/2)
			rnd2 = random.randint(length/2,length-1)
		tmp1[rnd1:rnd2],tmp2[rnd1:rnd2] = tmp2[rnd1:rnd2],tmp1[rnd1:rnd2]
		maincodes.append(tmp1)
		maincodes.append(tmp2)

def sortalive(ranktable):
	ranktable.sort(key=lambda rank: rank[1])
	print(ranktable[0][1])

def roulette(maincodes,ranktable,allzero):
	newlist = []
	cdef int i = 0
	while(len(newlist)<LEN_N):
		if(allzero > 750*LEN_B):
			per = random.randint(0,100)
			PER = 5
			if(per > ranktable[i][1]/allzero*100):
				newlist.append(maincodes[ranktable[i][0]])
				ranktable[i][1] = 9999
		else:
			newlist.append(maincodes[ranktable[i][0]])
		i += 1
	return newlist

def mutation(maincodes):
	cdef int i
	cdef int length = len(maincodes[0])
	cdef int rnd2
	cdef int rnd3
	cdef int rnd4
	for i in xrange(LEN_B-1):
		rnd1 = random.randint(0,100)
		if(rnd1 <= PER):
			maincodes[i+1][0:(length/2+1)] = maincode(length/2)

def putzero(lista,length):
	cdef int i
	cdef int j
	for i in xrange(length):
		lista.append([])
		for j in xrange(length):
			lista[i].append(0)
