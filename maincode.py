# coding:utf-8
import random

#$BMp?t$G(BMAIN$B%3!<%I(B
#$B0z?t(B:$B$J$7(B
#$BLa$jCM(B:MAIN$B%3!<%I(B	[[0],[1],[2],$B!&!&!&(B]
def maincode() :
 main=[]
 i=0
 while i<10 :

   main.append([random.randint(0,999),random.randint(0,999),random.randint(0,999)])

   i+=1

 return main

print maincode()
