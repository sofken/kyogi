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
  list1_size+=list1[i]*list1[i]
  list2_size+=list2[i]*list2[i]
  inner+=list1[i]*list2[i]
  i+=1
 return inner/(math.sqrt(list1_size)*math.sqrt(list2_size))
 
#IF_stage=[[一個目のベクトル],[二個目のベクトル],,,]]
#IF_stone=[[一個目のベクトル],[二個目のベクトル],,,]]
#Main_code=[[一個目のベクトル],[二個目のベクトル],,,]]
#Trimming_stage=[トリミングしたステージのベクトル]
#stone_now=[今の石のベクトル]

def test(IF_stage,IF_stone,Main_code,Trimming_stage,stone_now):
 IF_stage_number=len(IF_stage)
 IF_stone_number=len(IF_stone)
 Main_code_number=len(Main_code)
 Match_rate_stone_max=0
 Match_rate_stone_number=-1
 Match_rate_stage_max=0
 Match_rate_stage_number=-1
 now_Match_rate=0
 i=0
 while i<IF_stone_number:
  now_Match_rate=Match_rate(stone_now,IF_stone[i])
  if now_Match_rate>Match_rate_stone_max:
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
  if Main_code[i][0]==Match_rate_stone_number and Main_code[i][0]==Match_rate_stage_number:
   return Main_code[i][2]
  i+=1
 return -1

IF_stage=[[1,0,0,0]]
IF_stone=[[1,0,0,0]]
Main_code=[[0,0,0]]
Trimming_stage=[1,0,0,0]
stone_now=[1,0,0,0]
print test(IF_stage,IF_stone,Main_code,Trimming_stage,stone_now)
 
