# coding:utf-8
import random

#乱数でIF_STONEをつくる
#引数:なし
#戻り値:IFストーン

def IF_STONE():
 if_stone=[]
 k=0
 while k<1 :  #1 個つくる
   i=0
   if_stone.insert(k,[[],[],[],[],[],[],[],[]]) #リストの用意
   s=0

   while i<8 :
     j=0
     while j<8 :
       # s(1の数)が16以下なら 1,0 をいれる
       if s<16 :
         #乱数で値を入れる
         if_stone[k][i].append(random.randint(0,1))
         str(if_stone[k][i])
           # 1 のカウント
         if if_stone[k][i][j] == 1 :
            s+=1
         j+=1
         continue
       else :
         if_stone[k][i].append(0)
         j+=1
         continue

     i+=1
     continue

   k+=1
 print s
 return if_stone

print IF_STONE()
