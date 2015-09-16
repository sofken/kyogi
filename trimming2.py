# coding:utf-8

FilePass='/home/me1320/Desktop/Documents/sofken/python/test2.txt'

n=32

#txtからステージを読み込む関数
#引数:txtファイルのパス
#戻り値:多重リスト状態のステージリスト
def FileRead_stage(FilePass):
 i=0
 j=0
 char=''
 Read_stage=[]
 ForNow=[]
 fornow=0
 FileObject=open(FilePass,'r')
 while True :
  if i==n:
   Read_stage.append(ForNow)	
   ForNow=[]
   j+=1
   i=0
   FileObject.seek(2,1)	
  if j==n:
   break
  char=FileObject.read(1)
  fornow=int(char)
  ForNow.append(fornow)
  i+=1
 FileObject.close()
 return Read_stage  

#関数の結果を STAGE に置き換え
STAGE=FileRead_stage(FilePass)

#print STAGE


#2を探す関数	※2 は、自分ではめた石
#引数:ステージ
#戻り値:2の場所
def Find_side(STAGE):
 i=0
 Side=[]
 while i<n :
   j=0

   while j<n :
     if STAGE[i][j]==2 :
        Side.append([i,j])
       
     if j<n :
       j+=1
       continue

   i+=1
   continue

 return Side

#関数の結果を SIDE に置き換え
SIDE=Find_side(STAGE)

print SIDE


#ステージをトリミングする関数
#引数:2の位置、ステージの情報
#戻り値:トリミングしたステージ

def trimming(SIDE,STAGE):
 a=len(SIDE)
 k=0
 while k<a :
  #トリミングの初期位置
   SIDE[k][0]=SIDE[k][0]-4
   SIDE[k][1]=SIDE[k][1]-4
  #初期位置をBとおく
   B=SIDE[k]
   print B
   #t_stage=[]
   t_stage=[k,[],[],[],[],[],[],[],[],[]]   #[[]×9]

   i=SIDE[k][0]
  # j=SIDE[k][1]

   i1=SIDE[k][0]
   j1=SIDE[k][1]

   c = 0
   while i<i1+9 :
     #t_stage.append([k])
     j=SIDE[k][1]
     #c=0

     while j<j1+9 :
       t_stage[c+1].append(STAGE[i][j])
       j+=1
       #c+=1
       continue

     i+=1
     c+=1
     continue

   print t_stage
   t_stage=[k,[],[],[],[],[],[],[],[],[]]   #[[]×9]
   k+=1

 return 0

print trimming(SIDE,STAGE)
