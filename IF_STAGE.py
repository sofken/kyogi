# coding:utf-8
import random

#乱数でIF_STAGEをつくる
#引数:なし
#戻り値:IFステージ(多重リスト)	[ [ [],[],・・・],[ [],[],・・・] ]

def IF_STAGE():
 if_stage=[]
 k=0
 while k<2 :  #2個つくる
   i=0
   if_stage.insert(k,[[],[],[],[],[],[],[],[],[]]) #リストの用意

   while i<9 :
     j=0
     while j<9 :
      #乱数で値を入れる
       if_stage[k][i].append(random.randint(0,1))
       str(if_stage[k][i])
       j+=1
       continue

     i+=1
     continue

   k+=1

 return if_stage

print IF_STAGE()
