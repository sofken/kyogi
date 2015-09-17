import math
from copy import deepcopy
import random

def Match_rate(list1,list2):
 #import math
 list1_len=len(list1)
 list2_len=len(list2)
 if list1_len<>list2_len:
  return -1
 i=0
 list1_size=0
 list2_size=0
 inner=0
 while i<list1_len :
  list1_size+=int(list1[i])*int(list1[i])
  list2_size+=int(list2[i])*int(list2[i])
  inner+=int(list1[i])*int(list2[i])
  i+=1
 return inner/(math.sqrt(list1_size)*math.sqrt(list2_size))
 
#IF_stage=[[first],[second],,,]]
#IF_stone=[[first],[second],,,]]
#Main_code=[[first],[second],,,]]
#Trimming_stage=[trimming stage vector]
#stone_now=[now stone vector]

def test(IF_stage,IF_stone,Main_code,Trimming_stage,stone_now):
 IF_stage_number=len(IF_stage)
 IF_stone_number=len(IF_stone)
 Main_code_number=len(Main_code)
 Match_rate_stone_max=0 #the most semelar in stone(0-1)
 Match_rate_stone_number=-1 #the most semelar in stone index
 Match_rate_stage_max=0
 Match_rate_stage_number=-1
 now_Match_rate=0 #now sone(0-1)
 i=0
 while i<IF_stone_number:
  now_Match_rate=Match_rate(stone_now,IF_stone[i])
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
  if Main_code[i][0]==Match_rate_stone_number and Main_code[i][1]==Match_rate_stage_number:
   return Main_code[i][2]
  i+=1
 return -1

#get stage & stone data 0->stage 1~->stone
def getdata():
	f = open('sample2.txt','r')
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
  if i==0:
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
			print(zerox,zeroy,HT[act[2]*90],act[1]*90)
		else:
			change = '0'
			print(' ')
		for k in range(8):
			for l in range(8):
				if(stage[k+zeroy][l+zerox]=='3'):
					stage[k+zeroy][l+zerox] = change

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
				if(j+y<8 and k+x<8 and stone[j+y][k+x]=='1'):
					one = [k+x,j+y]
					#print(one)
					return one
				elif(y-j>-1 and x-k>-1 and stone[y-j][x-k] == '1'):
					one = [x-k,y-j]
					#print(one)
					return one
				if(y-j>-1 and k+x<8 and stone[y-j][k+x]=='1'):
					one = [k+x,y-j]
					#print(one)
					return one
				elif(j+y>-1 and x-k>-1 and stone[j+y][x-k] == '1'):
					one = [x-k,j+y]
					#print(one)
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

#stone & stage reading
data = getdata() #stage & stone two data
onedata = []
for i in range(len(data)):
	onedata.append(getone(data[i])) #stage & stone one data
twostage = data[0]
addone(twostage)
del data[0]
onestage = getone(twostage)
del onedata[0]

stonelen = len(data)
#put stone & output
for n in range(stonelen):
	#tromming datas
	side=Find_side(twostage)
	sidelen = len(side)
	tristage = trimming(side,twostage)

	#codes
	IF_stage = tristage
	IF_stone = onedata #templary IF = getdata
	act = [[[1,3],0,0],[[4,6],2,0],[7,7],7,7]
	Main_code = [[1,0,0],[1,1,1]]
	stone_now=onedata[1]

	random.seed()
	rnd = random.randint(0,sidelen-1)
	action = test(IF_stage,IF_stone,Main_code,tristage[0],stone_now)
	putstone(twostage,data[n],[side[rnd][1][0]+4,side[rnd][1][1]+4],side[rnd][0],act[action])
	viewstage(twostage)
