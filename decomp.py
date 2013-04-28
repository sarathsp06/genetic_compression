from os import system 
from PIL import Image
from ctypes import c_int16
import pickle
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
                        #print len(p),len(q)
                        k=0
                        for w in p:
                                data[i][j][k]=int(w)	
                                k+=1
                                #print w
                        for w in q:
                                data[i][j][k]=int(w)
                                k+=1
                                #print w
       #for i in range(64):
       #         for j in range(64):
       #                 print data[i][j]                        
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
                            L[i][j][k] = blist[acnt]
                        elif L[i][j][k] == 0:
                            L[i][j][k] = alist[acnt]
        #for i in range(64):
         #       for j in range(64):
         #               print L[i][j]
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


Lred=decompress(Lred,LalistR,LblistR)
Lblue=decompress(Lblue,LalistB,LblistB)
Lgreen=decompress(Lgreen,LalistG,LblistG)
#system("del *.dat")



img = Image.new( 'RGB', (256,256), "white") # create a new white image
#img.show()
L=[[[]for i in range(64)] for j in range(64)]
L=[[[(Lred[i][j][k],Lgreen[i][j][k],Lblue[i][j][k]) for k in range(16) ]for i in range(64)] for j in range(64)]
for i in range(256):
    for j in range(256):
        img.putpixel((i,j),L[int(i/4)][int(j/4)][int((i%4)*4+(j%4))])


img.save('dlena.bmp')
img.show()
