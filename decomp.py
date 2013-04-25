from os import system 
from PIL import Image
from ctypes import c_int16
import pickle
import genetic

def load_file(filename):        
        fin=open(filename+".dat",'r+b')
        data=[[[p for p in range(16)]for j in range(64)]for i in range(64)]
        for i in range(64):
                for j in range(64):
                        p=str(bin(ord(fin.read(1))))[2:]
                        a='0'*(8-len(p))
                        p=a+p
                        q=str(bin(ord(fin.read(1))))[2:]
                        a='0'*(8-len(q))
                        q=a+q
                        k=0
                        for w in p:
                                data[i][j][k]=int(w)	
                                k+=1
                           
                        for w in q:
                                data[i][j][k]=int(w)
                                k+=1
                                           
        return data

def load_int(filename):        
        fin=open(filename+".dat",'r+b')
        L=[]
        dat=fin.read(1)
        while dat != '':
                L.append(ord(dat))
                dat=fin.read(1)
        return L

def decompress(L,alist,blist):
        acnt=-1
        for i in range(64):
                for j in range(64):
                    acnt+=1
                    for k in range(16):
                        if L[i][j][k] == 1:
                            L[i][j][k] = alist[acnt]
                        elif L[i][j][k] == 0:
                            L[i][j][k] = blist[acnt]
        return L

Lred=load_file('redlayer')
Lblue=load_file('bluelayer')
Lgreen=load_file('greenlayer')

LalistR=load_int('ared')
LalistB=load_int('ablue')
LalistG=load_int('agreen')

LblistR=load_int('bred')
LblistB=load_int('bblue')
LblistG=load_int('bgreen')

Rmse=load_int('Rm')
Gmse=load_int('Gm')
Bmse=load_int('Bm')

Lred=decompress(Lred,LalistR,LblistR)
Lblue=decompress(Lblue,LalistB,LblistB)
Lgreen=decompress(Lgreen,LalistG,LblistG)

#"""
Lred=[[genetic.make_block(LalistR[i*64+j],LblistR[i*64+j],Lred[i][j],Rmse[i*64+j])for j in range(64)]for i in range(64)]
Lgreen=[[genetic.make_block(LalistG[i*64+j],LblistG[i*64+j],Lgreen[i][j],Gmse[i*64+j])for j in range(64)]for i in range(64)]
Lblue=[[genetic.make_block(LalistB[i*64+j],LblistB[i*64+j],Lblue[i][j],Bmse[i*64+j])for j in range(64)]for i in range(64)]
#"""

img = Image.new( 'RGB', (256,256), "white") # create a new white image
L=[[[]for i in range(64)] for j in range(64)]
L=[[[(int(round(Lred[i][j][k])),int(round(Lgreen[i][j][k])),int(round(Lblue[i][j][k]))) for k in range(16) ]for i in range(64)] for j in range(64)]
for i in range(256):
    for j in range(256):
        img.putpixel((i,j),L[int(i/4)][int(j/4)][int((i%4)*4+(j%4))])
img.save('dlena.bmp')
img.show()
