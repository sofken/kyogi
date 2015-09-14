import math
from copy import deepcopy

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
  now_Match_rate=Match_rate(Trimming_stage,IF_stage[i])
  if now_Match_rate>Match_rate_stage_max:
   Match_rate_stage_number=i
   Match_rate_stage_max=now_Match_rate
  i+=1
 i=0
 while i<Main_code_number:
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

#ABC -> A,B,C
def twotoone(two):
	onedata = ""
	onelist = []
	for tmp in two:
		onedata += (tmp + ",")
	onedata = onedata[:-1]
	onelist = [onedata]
	return onedata

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
#def putstone(stage,stone,coor,dire,act):
	#coor(coordinate)...(X,Y)
	#dire(direction)...1(up) 2(bottom) 3(left) 4(right)

	#operate against stone

#ooll vector
def roll(stone,times):
	rollstone = deepcopy(stone)
	for i in range(8):
		for j in range(8):
			nexti = j
			nextj = 7-i
			rollstone[nexti][nextj] = stone[i][j]
	return rollstone

data = getdata() #stage & stone two data
onedata = []
for i in range(len(data)):
	onedata.append(getone(data[i])) #stage & stone one data
twostage = data[0]
del data[0]
onestage = onedata[0]
del onedata[0]
print(data[0])
print(roll(data[0],0))
IF_stage = [[1,0,0,0]]
IF_stone = onedata #templary IF = getdata
Main_code = [[0,0,1],[1,0,2]]
Trimming_stage = [1,0,0,0]
stone_now=onedata[1]
#print test(IF_stage,IF_stone,Main_code,Trimming_stage,stone_now)
