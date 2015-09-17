# coding:utf-8
import random

#乱数でMAINコード
#引数:なし
#戻り値:MAINコード	[[0],[1],[2],・・・]
def maincode() :
 main=[]
 i=0
 while i<10 :

   main.append([random.randint(0,999),random.randint(0,999),random.randint(0,999)])

   i+=1

 return main

print maincode()
