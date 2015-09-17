# coding:utf-8
import random

#乱数でACTコード
#引数:なし
#戻り値:ACTコード	[ [ [1,2],1,0 ],[ [3,7],0,1 ],・・・] ]
def actcode() :
 act=[]
 i=0
 while i<10 :

   act.append([[random.randint(0,7),random.randint(0,7)],random.randint(0,3),random.randint(0,1)])

   i+=1

 return act

print actcode()
