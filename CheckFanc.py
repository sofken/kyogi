def Check(stage,stone,FilePass):
 FileObject=open(FilePass,'r')
 stone_len=len(stone)
 check_stone=[]
 cut_stage=CUT(stage,32)
 i=0
 while i<stone_len:
 check_stone.append([])
 i+=1
 now_stone_number=0
 for line in FileObject:
  if len(line)<3:
   now_stone_number+=1
   if now_stone_number==stone_len:
    break
   continue
  j=0
  k=0
  i=0
  while line[i]<>'/r':
   if line[i]==' ':
    if k<>2 and  k<>3:
     check_stone[now_stone_number].append(int(line[j:i]))
    elif k==2:
     if line[i-1]=='H':
      check_stone[now_stone_number].append(0)
     elif line[i-1]=='T':
      check_stone[now_stone_number].append(1)
    elif k==3:
     check_stone[now_stone_number].append(int(line[j:i])/90)
    j=i+1
    k+=1
   i+=1
  now_stone_number+=1
  if now_stone_number==stone_len:
   break
 FileObject.close()
 i=0
 j=0
 k=0
 while i<stone_len:
  j=0
  k=0
  if check_stone[i]==[]:
   i+=1
   continue
  if check_stone[i][2]==1:
   Reverse_stone(stone,i)
  while j<check_stone[i][2]:
   Right_Turn_stone(stone,i)
   j+=1
  j=0
  k=0
  while j<8:
   k=0
   while k<8:
    cut_stage[j+check_stone[i][1]][k+check_stone[1][0]]+=stone[i][j][k]
    k+=1
   j+=1
  i+=1
 return connect_stage(cut_stage)

def CUT(list1,cut_size):
 Cut_list=[]
 i=0
 k=cut_size
 while k<=cut_size*cut_size:
  Cut_list.append(list1[i:k])
  i+=cut_size
  k+=cut_size
 return Cut_list

def Connect_stage(stage):
 return [e for inner_list in stage for e in inner_list]

def Reverse_stone(stone,stone_Number):
 stone=Cut_stone(stone)
 stone_len=len(stone[0][0])
 i=0
 ForNow=[]
 while i<stone_len :
  j=stone_len-1
  fornow=[]
  while j>=0:
   fornow.append(stone[stone_Number][i][j])
   j-=1
  ForNow.append(fornow)
  i+=1
 stone[stone_Number]=ForNow
 stone=Connect_stone(stone)
 return stone
 
def Right_Turn_stone(stone,stone_Number):
 stone=Cut_stone(stone)
 stone_len=len(stone[0])
 i=0
 ForNow=[]
 while i<stone_len:
  j=stone_len-1
  fornow=[]
  while j>=0:
   fornow.append(stone[stone_Number][j][i])
   j-=1
  ForNow.append(fornow)
  i+=1
 stone[stone_Number]=ForNow
 stone=Connect_stone(stone)
 return stone
 
def Cut_stone(stone,stone_size=8):
 stone_number=len(stone)
 i=0
 while i<stone_number:
  k=0
  j=stone_size
  ForNow=[]
  while j<=stone_size*stone_size:
   ForNow.append(stone[i][k:j])
   k+=stone_size
   j+=stone_size
  stone[i]=ForNow
  i+=1
 return stone
