# coding:utf-8
import random

#$BMp?t$G(BACT$B%3!<%I(B
#$B0z?t(B:$B$J$7(B
#$BLa$jCM(B:ACT$B%3!<%I(B	[ [ [1,2],1,0 ],[ [3,7],0,1 ],$B!&!&!&(B] ]
def actcode() :
 act=[]
 i=0
 while i<10 :

   act.append([[random.randint(0,7),random.randint(0,7)],random.randint(0,3),random.randint(0,1)])

   i+=1

 return act

print actcode()
