#! /usr/bin/python
from random import choice, randint,Random
import numpy as np
from time import sleep

def random_chromosome(a,b,block):
	A=Random()
	chrome=[]
	if a == b:
		chrome = [a for i in range(16)]
		return chrome
	for i in range(16):
		try:
			if block[i] == 0:
				chrome.append(choice(range(a,int((a+b)/2))))
			else:
				chrome.append(choice(range(int((a+b)/2),b)))
		except:
			print "Exeption:",a,b
			exit()
	return chrome

def calc_fitness(L,a,b,MSE):                #assuming a is karger than b
        M=float(0)
        for k in range(16):
                if L[k] < (a+b)/2:
                        M+=(L[k]-a)**2
                else:
                        M+=(L[k]-b)**2
	M=(M/16)**0.5
        return abs(M-MSE)
 

def mate(chromo1,chromo2):#whole block
    	chromo=chromo1
	index=choice(range(16))
	c = choice((1,2))
	if c == 1:
                for i in range(index,16):
                        chromo[i]=int((chromo1[i]+chromo2[i])/2)
        else:
                for i in range(index):
                        chromo[i]=int((chromo2[i]+chromo1[i])/2)
	return chromo

def alphas(arrs,a,b,MSE):
    decorated = [(calc_fitness(chromo,a,b,MSE), chromo) for chromo in arrs]
    decorated.sort()
    return [chromo[1] for chromo in decorated][:10]
 

def make_block(a,b,Block,MSE):
	#print "_____________________________New Block_______________________________"
	NUM_OFFSPRING = 20
	SEEDS = [random_chromosome(a,b,Block) for i in range(NUM_OFFSPRING)]
	top10 = alphas(SEEDS,a,b,MSE)
	i = 0
	while i < 50:
	#	print i,"th epoch"
		offspring = [mate(choice(top10),choice(top10)) for j in range(NUM_OFFSPRING)]
               # for j in range(NUM_OFFSPRING):
                #        offspring.append(mate(choice(top10), choice(top10)))
                top10 = alphas(offspring,a,b,MSE)
		i += 1
		top10.sort()
	best=top10[0]
        return best




"""""

A=[[[a[i][j],b[i][j],make_block(L[i][j],MSE[i][j])]for j in range(64)]for i in range(64)]


"""""""""
