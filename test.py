import math

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
			tmpdata.append(line)
	return data	

#[ABC,DEF,GHI] -> ABCDEFGHI
def twotoone(two):
	onedata = ""
	for tmp in two:
		onedata += tmp
	return onedata

#two data -> one data
def getone(two):
	tmpdata = ""
	onedata = []
	for tmp in two:
		onedata.append(twotoone(tmp))
	return onedata

data = getdata() #stage & stone two data
onedata = getone(data) #stage & stone one data
stage = onedata[0]
del onedata[0]
IF_stage = [[1,0,0,0]]
IF_stone = onedata #templary IF = getdata
Main_code = [[0,0,1],[1,0,2]]
Trimming_stage = [1,0,0,0]
stone_now=onedata[1]
print test(IF_stage,IF_stone,Main_code,Trimming_stage,stone_now)
