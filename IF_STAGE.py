# coding:utf-8
import random

#$BMp?t$G(BIF_STAGE$B$r$D$/$k(B
#$B0z?t(B:$B$J$7(B
#$BLa$jCM(B:IF$B%9%F!<%8(B($BB?=E%j%9%H(B)	[ [ [],[],$B!&!&!&(B],[ [],[],$B!&!&!&(B] ]

def IF_STAGE():
 if_stage=[]
 k=0
 while k<2 :  #2$B8D$D$/$k(B
   i=0
   if_stage.insert(k,[[],[],[],[],[],[],[],[],[]]) #$B%j%9%H$NMQ0U(B

   while i<9 :
     j=0
     while j<9 :
      #$BMp?t$GCM$rF~$l$k(B
       if_stage[k][i].append(random.randint(0,1))
       str(if_stage[k][i])
       j+=1
       continue

     i+=1
     continue

   k+=1

 return if_stage

print IF_STAGE()
