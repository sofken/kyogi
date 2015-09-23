import math
from copy import deepcopy
import random
import numpy as np

def Match_rate(list1,list2):
 #import math
 list1_len=len(list1)
 list2_len=len(list2)
 if list1_len<>list2_len:
  return -1
 i=0
 #list1_size=0
 #list2_size=0
 nplist1 = np.array([list1],np.float)
 nplist2 = np.array([list2],np.float)
 nplist12 = np.array(list1,np.float)
 nplist22 = np.array(list2,np.float)
 list1_size = np.linalg.norm(nplist1)
 list2_size = np.linalg.norm(nplist2)
 inner=np.dot(nplist12,nplist22)
 #while i<list1_len :
  #list1_size+=int(list1[i])*int(list1[i])
  #list2_size+=int(list2[i])*int(list2[i])
  #i[nner+=int(list1[i])*int(list2[i])
  #i+=1
 return inner/(math.sqrt(list1_size)*math.sqrt(list2_size))
 
#IF_stage=[[first],[second],,,]]
#IF_stone=[[first],[second],,,]]
#Main_code=[[first],[second],,,]]
#Trimming_stage=[trimming stage vector]
#stone_now=[now stone vector]

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
  now_Match_rate=Match_rate(stone_now,getone(IF_stone[i]))
  if now_Match_rate>Match_rate_stone_max: #rewrite semelar
   Match_rate_stone_number=i
   Match_rate_stone_max=now_Match_rate
  i+=1
 i=0
 while i<IF_stage_number:
  now_Match_rate=Match_rate(getone(Trimming_stage),getone(IF_stage[i]))
  if now_Match_rate>Match_rate_stage_max:
   Match_rate_stage_number=i
   Match_rate_stage_max=now_Match_rate
  i+=1
 i=0
 Match_rate_stone_ma = round(Match_rate_stone_max,1)
 Match_rate_stone_ma = round(Match_rate_stage_max,1)
 while i<Main_code_number:
  #print(Match_rate_stone_number,Match_rate_stage_number)
  #print(Main_code[i])
  if Main_code[i][0]==Match_rate_stone_number and Main_code[i][1]==Match_rate_stage_number:
   return Main_code[i][2]
  i+=1
 return -1

#get stage & stone data 0->stage 1~->stone
def getdata():
	f = open('sample.txt','r')
	tmpdata = []
	data = []
	i = 0
	
	for line in f:
		if(len(line)==2):
			data.append(tmpdata)
			tmpdata = []
		elif(len(line)!=4):
			line = line.rstrip('\r\n')
			tmpdata.append(list(line))
	return data	

#two data -> one data
def getone(two):
	twolen = len(two)
	cptwo = deepcopy(two)
	for i in range(twolen-1):
		cptwo[0].extend(cptwo[i+1])
	return cptwo[0]

def Conversion(list1):
 i=0
 list2=[]
 for i in list1:
  if i==2:
   list2.append(1)
  else :
   list2.append(i)
 return list2

def Count_0(list1):
 Count=0
 i=0
 for i in list1:
  for j in i:
   if j=='0':
    Count+=1
 return Count

#put stone
def putstone(stage,stone,coor,dire,act):
	#coor(coordinate)...(X,Y)
	#dire(direction)...1(up) 2(bottom) 3(left) 4(right)

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
		for i in range(8):
			for j in range(8):
				if(stage[i+zeroy][j+zerox]=='0' and cpstone[i][j]=='1'):
						stage[i+zeroy][j+zerox] = '3'
				elif((stage[i+zeroy][j+zerox]=='1' or stage[i+zeroy][j+zerox]=='2') and cpstone[i][j]=='1'):
					passes = 0
					break
	
		HT=['H','T']
		#3->2 or 3->1
		if(passes == 1):
			change = '2'
			print(zerox,zeroy,HT[act[2]],act[1]*90)
		else:
			change = '0'
			print(' ')
		for k in range(8):
			for l in range(8):
				if(stage[k+zeroy][l+zerox]=='3'):
					stage[k+zeroy][l+zerox] = change
		print(passes)
		return passes
	else:
		return 0

#roll vector
def roll(stone,times):
	rollstone = deepcopy(stone)
	copystone = deepcopy(stone)
	for k in range(times):
		for i in range(8):
			for j in range(8):
				nexti = j
				nextj = 7-i
				rollstone[nexti][nextj] = copystone[i][j]
		copystone = deepcopy(rollstone)
	return copystone

#change left and right
def lrchange(stone):
	changestone = deepcopy(stone)
	for i in range(8):
		for j in range(8):
			nextj = 7 - j
			changestone[i][nextj] = stone[i][j]
	return changestone

#add many 1
def addone(stage):
	for i in range(32):
		for j in range(10):
			stage[i].append('1')
	for k in range(10):
		stage.append([])
		for l in range(42):
			stage[k+32].append('1')

#find 1 in stone
def findone(stone,x,y):
	for i in range(8):
		for j in range(i):
			for k in range(i):
				#print(j,x,y)
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

def Find_side(STAGE):
	n=32
	i=0
	Side=[]
 	for j in range(n) :
		for i in range(n):
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
			t_stage[k].append([])
			j=SIDE[k][1][0]

			while j<j1+9 :
				t_stage[k][c].append(STAGE[i][j])
				j+=1
				continue

			i+=1
			c+=1
			continue

		k+=1

	return t_stage

#View Stage for DEBUG
def viewstage(twostage):
	for i in range(32):
		line = ""
		for j in range(32):
			line += twostage[i][j]
		print(line)

#search first step
def putfirst(stage,data,IF_stage,IF_stone,act,Main_code,n):
	twolist = []
	for i in range(32):
		for j in range(32):
			if(stage[i][j]=='1'):
				if(stage[i-1][j] == '0' or stage[i][j-1] == '0' or stage[i+1][j] == '0' or stage[i][j+1] == '0'):
					stage[i][j] = '2'
					twolist.append([i,j])
	res = putting(stage,data,IF_stage,IF_stone,act,Main_code,n)
	#viewstage(twostage)
	for k in twolist:
		stage[k[0]][k[1]] = '1'
	return res


def IF_STAGE():
 if_stage=[]
 k=0
 while k<100 :  #2個つくる
   i=0
   if_stage.insert(k,[[],[],[],[],[],[],[],[],[]]) #リストの用意

   while i<9 :
     j=0
     while j<9 :
      #乱数で値を入れる
       if_stage[k][i].append(str(random.randint(0,1)))
       j+=1
       continue

     i+=1
     continue

   k+=1

 return if_stage
def IF_STONE():
 if_stone=[]
 k=0
 while k<100 :  
   i=0
   if_stone.insert(k,[[],[],[],[],[],[],[],[]]) 

   while i<8 :
     j=0
     while j<8 :
      
       if_stone[k][i].append(str(random.randint(0,1)))
       j+=1
       continue

     i+=1
     continue

   k+=1

 return if_stone
def actcode() :
 act=[]
 i=0
 while i<1000 :

   act.append([[random.randint(0,7),random.randint(0,7)],random.randint(0,3),random.randint(0,1)])

   i+=1

 return act

def maincode() :
 main=[]
 i=0
 a = []
 b = []
 while i<9000 :
   passes = 0
   arnd = random.randint(0,99)
   brnd = random.randint(0,99)
#   while(i!=0 and passes==0):
#	   arnd = random.randint(0,99)
#	   brnd = random.randint(0,99)
#	   for j in range(len(a)):
#		   if(a[j]==arnd and b[j]==brnd):
#			   passes = 0
#			   break
#		   else:
#			   passes = 1
   
   a.append(arnd)
   b.append(brnd)
   main.append([arnd,brnd,random.randint(0,999)])

   i+=1
 return main

def putting(stage,data,IF_stage,IF_stone,act,Main_code,n):
	side=Find_side(stage)
	sidelen = len(side)
	tristage = trimming(side,stage)
	res = 0 #0...loop
	times = 0
	while(res==0 and times<1):
		random.seed()
		rnd = random.randint(0,sidelen-1)
		action = test(IF_stage,IF_stone,Main_code,tristage[rnd],getone(data[n]))
		res = putstone(stage,data[n],[side[rnd][1][0]+4,side[rnd][1][1]+4],side[rnd][0],act[action])
		times += 1
	return res



#Genetic algorithm	
#contents
LEN_N = 2 #Main code len
LEN_B = 5 #After born Main code len
TARGET = 20
DEATH = 4 #not death percentage
PER = 5 #not mutation percentage

#radian -> x
def work(stage,data,IF_stage,IF_stone,act,Main_code):
	#first
	i = 0
	res = 0
	stonelen = len(data)
	while(res==0 and i<stonelen):
		res = putfirst(stage,data,IF_stage,IF_stone,act,Main_code,i)
		i += 1
	#put stone & output
	
	for n in range(stonelen-i):
	#for n in [i]:
		#tromming datas
		putting(stage,data,IF_stage,IF_stone,act,Main_code,n+i)
		#viewstage(twostage)
	
	zero = Count_0(stage)
	viewstage(stage)
	return zero
	#viewstage(twostage)
	#random in 0-180

#check stop revoluation
def check_stop(lista,ranktable,cpstage,data,IF_stage,IF_stone,act):
	go = 1
	j = 0
	for i in lista:
		cpstage = deepcopy(twostage)
		zero = work(cpstage,data,IF_stage,IF_stone,act,i)
		ranktable.append([j,zero])
		if zero <= TARGET: #warning
			go = 0
		j += 1
	return go

#Crossing
def crossing(lista):
	for i in range(LEN_B-LEN_N):
		one = 0
		two = 0
		while one == two:
			one = random.randint(0,LEN_N-1)
			two = random.randint(0,LEN_N-1)
		tmp1 = deepcopy(lista[one])
		tmp2 = deepcopy(lista[two])
		for j in range(1000):
			rnd = random.randint(0,8996)
			tmp1[rnd],tmp2[rnd] = tmp2[rnd],tmp1[rnd]
			tmp1[rnd+1],tmp2[rnd+1] = tmp2[rnd+1],tmp1[rnd+1]
			tmp1[rnd+2],tmp2[rnd+2] = tmp2[rnd+2],tmp1[rnd+2]
		lista.append(tmp1)
		lista.append(tmp2)

#sort(aliving)
def sortalive(ranktable):
	ranktable.sort(key=lambda rank: rank[1])

#death in roulette
def roulette(lista):
	i = LEN_B - LEN_N
	j = 0
	dellist = []
	while i>0:
		rnd = random.randint(0,100)
		if(rnd < j*DEATH):
			dellist.append(ranktable[j][0])
			del ranktable[j]
			i -= 1
		if(j < LEN_N-1+i):
			j += 1
		else:
			j = 0

	l = 0
	for k in dellist:
		del lista[k+l]
		l -= 1

def checkdel(target,listb):
	for i in listb:
		if(i==target):
			return 0
		else:
			return 1

#output excellence
def excell(lista):
	maximam = 0
	maximam_ind = 0
	for i in range(LEN_N):
		now = work(lista[i][0],degtorad(lista[i][1]),lista[i][2])
		if(now > maximam):
			maximam = now
			maximam_ind = i
	print(maximam)
#	print(maximam_ind)

#mutation
def mutation(lista):
	for i in range(LEN_B):
		rnd = random.randint(0,LEN_B)
		if(rnd > PER):
			lista[i] = maincode() 
	return lista





#stone & stage reading
#data     = two stone
#onedata  = one stone
#twostage = two stage
#onestage = one stage
data = getdata() #stage & stone two data
onedata = []
for i in range(len(data)):
	onedata.append(getone(data[i])) #stage & stone one data
twostage = data[0]

addone(twostage)
del data[0]
onestage = getone(twostage)
del onedata[0]

#codes
IF_stage = IF_STAGE()
IF_stone = IF_STONE()
act = actcode()
act.append([[7,7],7,7])
Main_code = []
print('start create maincode ...')
for i in range(LEN_N):
	Main_code.append(maincode())
print('finish create maincode ...')

cpstage = deepcopy(twostage)
go= 1

ranktable = []
while(go):
	print('start crossing ...')
	crossing(Main_code)
	print('start mutation ...')
	mutation(Main_code)
	print('start checking ...')
	go = check_stop(Main_code,ranktable,cpstage,data,IF_stage,IF_stone,act)
	print('start sort .............................................')
	sortalive(ranktable)
	print('start roulette ...')
	roulette(Main_code)
	print('start checking ...')
	go = check_stop(Main_code,ranktable,cpstage,data,IF_stage,IF_stone,act)
	viewstage(cpstage)
	ranktable = []
