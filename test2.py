import math

def First_search(stage_list):
 #import math
 Trimming_xy=[]
 Trimming_size=9#トリミングの大きさ(奇数)
 center_xy=int(Trimming_size/2)
 Number_0=Count_0(stage_list)
 Standard_Barrier_Rate=25#後で変更(障害物が多いか少ないかの基準(1〜100%))
 stage_len=len(stage_list)
 stage_size=math.sqrt(stage_len)
 Barrier_Rate=(stage_len-Number_0)/stage_size*100
 flag=-1#0:Center 1:Corner
 most_0=Dist(stage_list)
 if Barrier_Rate==0:#障害物ゼロのときは左上角
  return [[center_xy,center_xy]]
 if(Barrier_Rate>Standard_Barrier_Rate):
  flag=0
 else:
  flag=1
 Trimming_xy=[]
 left=int(math.ceil(stage_size/2)-1)
 right=int(math.floor(stage_size/2))
 center=[[left,left],[right,left],[right,right],[left,right]]
 center_around=[[left-center_xy,left-center_xy],[right+center_xy,left-center_xy],[right+center_xy,right+center_xy],[left-center_xy,right+center_xy]]
 side=[[],[],[],[]]
 side[0]=[[center_xy,center_xy],[left-center_xy,center_xy],[left-center_xy,left-center_xy],[center_xy,left-center_xy]]
 side[1]=[[right+left-center_xy,center_xy],[right+left-center_xy,left-center_xy],[right+center_xy,left-center_xy],[right+center_xy,left-center_xy]]
 side[2]=[[right+left-center_xy,right+left-center_xy],[right+center_xy,right+left-center_xy],[right+center_xy,right+center_xy],[right+left-center_xy,right+center_xy]]
 side[3]=[[center_xy,right+left-center_xy],[center_xy,right+center_xy],[left-center_xy,right+center_xy],[left-center_xy],[right+left-center_xy]]
 Trimming_yx=[]
 if flag==0:
  i=0
  while i<4:
   Trimming_yx.append(center[most_0[i]])
   i+=1
  i=0
  while i<4:
   Trimming_yx.append(center_around[most_0[i]])
   i+=1
 if flag==1:
  i=0
  while i<4:
   Trimming_yx.extend(side[most_0[i]])
   i+=1
 return Trimming_yx
  
 
 
 
def Dist(list1):
 #import math
 stage_size=int(math.sqrt(len(list1)))
 cut_stage=CUT(list1,stage_size)
 center_left=int(math.ceil(stage_size/2)-1)
 center_right=int(math.floor(stage_size/2))
 Number_0=[0,0,0,0]
 most_direct=[]
 i=0
 while i<stage_size:
  j=0
  while j<stage_size:
   if cut_stage[i][j]==0:
    if i<=center_left and j<=center_left:
     Number_0[0]+=1
    if i>=center_right and j<=center_left:
     Number_0[1]+=1
    if i>=center_right and j>=center_right:
     Number_0[2]+=1
    if i<=center_left and j>=center_right:
     Number_0[3]+=1
   j+=1
  i+=1 
 i=0
 j=0
 while j<4:
  i=0
  most_number=0
  most=Number_0[0]
  while i<4: 
   if most<Number_0[i]:
    most=Number_0[i]
    most_number=i
   i+=1
  most_direct.append(most_number)
  Number_0[most_number]=0
  j+=1
 return most_direct

def CUT(list1,cut_size):
 Cut_list=[]
 i=0
 k=cut_size
 while k<=cut_size*cut_size:
  Cut_list.append(list1[i:k])
  i+=cut_size
  k+=cut_size
 return Cut_list
 
def FileRead_stage(FilePass):
 i=0
 j=0
 char=''
 Read_stage=[]
 ForNow=[]
 fornow=0
 FileObject=open(FilePass,'r')
 while True :
  if i==32:
   Read_stage.append(ForNow)	
   ForNow=[]
   j+=1
   i=0
   FileObject.seek(2,1)	
  if j==32:
   break
  char=FileObject.read(1)
  fornow=int(char)
  ForNow.append(fornow)
  i+=1
 FileObject.close()
 return Connect_stage(Read_stage)  
 
def Connect_stage(stage):
 return [e for inner_list in stage for e in inner_list]
 
def Count_0(list1):
 Count=0
 i=0
 for i in list1:
  if i==0:
   Count+=1
 return Count
 
FilePass='/home/el1414/Desktop/Documents/quest1.txt'
stage=FileRead_stage(FilePass)
print First_search(stage)
