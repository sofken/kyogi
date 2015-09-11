from math import *
import random

random.seed()

#contents
MINN1 = 1
MAXN1 = 10
MINN2 = 1
MAXN2 = 179
MINN3 = 9
MAXN3 = 10
LEN_N = 10
LEN_B = 20
TARGET = 11
DEATH = 4 #not death percentage
PER = 5 #not mutation percentage

#degrees -> radian
def degtorad(rad):
	return rad*pi/180 

#radian -> x
def work(speed,rad,g):
	time = 2*speed*sin(rad)/g
	return speed*cos(rad)*time

#random in 0-180
def randmake(lista):
	return [random.randint(MINN1,MAXN1),random.randint(MINN2,MAXN2),random.randint(MINN3,MAXN3)]

#make list (all 0)
def listmake(lista,length):
	i = 0
	while i<length:
		lista.append(0)
		i+=1
	return lista

#check stop revoluation
def check_stop(lista):
	stop = 1
	for i in lista:
		if work(i[0],degtorad(i[1]),i[2]) >= TARGET:
			stop = 0
	return stop

#Crossing
def crossing(lista):
	for i in range((LEN_B-LEN_N)/2):
		first = 0
		second = 0
		while first == second:
			first = random.randint(0,LEN_N-1)
			second = random.randint(0,LEN_N-1)
		lista.append([lista[first][0],lista[second][1],lista[first][2]])
		lista.append([lista[second][0],lista[first][1],lista[second][2]])
	return lista

#sort(aliving)
def sortalive(lista):
	for i in range(LEN_B-1):
		maximam = 0
		j = i + 1
		while(j<LEN_B):
			if(work(lista[i][0],degtorad(lista[i][1]),lista[i][2]) < work(lista[j][0],degtorad(lista[j][1]),lista[j][2])):
				lista[i],lista[j] = lista[j],lista[i]
			j += 1
	return lista

#death in roulette
def roulette(lista):
	i = LEN_B - LEN_N
	j = 0
	while i>0:
		rnd = random.randint(0,100)
		if(rnd < j*DEATH):
			del lista[j]
			i -= 1
		if(j < 9+i):
			j += 1
		else:
			j = 0
	return lista

#output excellence
def excell(lista):
	maximam = 0
	maximam_ind = 0
	for i in range(LEN_N):
		now = work(lista[i][0],degtorad(lista[i][1]),lista[i][2])
		if(now > maximam):
			maximam = now
			maximam_ind = i
	print(maximam)
#	print(maximam_ind)

#mutation
def mutation(lista):
	for i in range(LEN_B):
		rnd = random.randint(0,100)
		if(rnd > PER):
			lista[i] = [random.randint(MINN1,MAXN1),random.randint(MINN2,MAXN2),random.randint(MINN3,MAXN3)]
	return lista


gem = []
gem = listmake(gem,LEN_N)
gem2 = map(randmake,gem)
while check_stop(gem2):
	gem2 = crossing(gem2)
	gem2 = sortalive(gem2)
	gem2 = mutation(gem2)
	gem2 = roulette(gem2)
	excell(gem2)
#print(gem2)
#excell(gem2)
