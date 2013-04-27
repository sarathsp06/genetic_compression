#!/usr/bin/python
from os import system 
from PIL import Image
from ctypes import c_int16
from os import chdir,path
def compress(L):  
    meanlist=[]
    malphalist=[]
    mcount=0
    qcount=0
    qlist=[]
    malpha=0
#print len(L),"--",len(L[0]),"===",len(L[0][2])
#print L[0][0],"\n------------------\n",L[63][63]
    #print L[0][0]
    for i in range(64):
        for j in range(64):
            avg=float(sum(L[i][j]))/16
            meanlist.append(avg)
            mcount+=1
            qlist.append(qcount) #starts from qlist[i+1]
            qcount=0
            malphalist.append(malpha)#starts from malphalist[i+1],4096 limit
            malpha=0
            for k in range(16):
                if L[i][j][k]>avg:
                    qcount+=1
                malpha=malpha+abs(L[i][j][k]-avg)
                if L[i][j][k]<avg:
                    L[i][j][k]=0
                else:
                    L[i][j][k]=1
    malphalist.append(malpha)
    qlist.append(qcount)
    #print malphalist[1]
    #for i in range(64):
     #   for j in range(64):
      #      print L[i][j]
    alist=[]
    blist=[]
    res=0
    for i in range(4096):
        if (16-qlist[i]==0):
            alist.append(round(meanlist[i]))
        else:
            res=meanlist[i]-float((malphalist[i+1]/(2*(16-qlist[i+1]))))
            alist.append(round(res))
    for i in range(4096):
        if qlist[i+1]!=0:
            res=meanlist[i]+float((malphalist[i+1]/(2*qlist[i+1])))
            blist.append(round(res))
        else:
            blist.append(round(meanlist[i]))
    #for i in range(4096):
    print blist[0]
    #print min(alist),max(alist)
    #print min(blist),max(blist)
    return L,alist,blist


def store(L,filename):
    compressed=[]
    f=open(filename+".dat",'w+b')
    for i in range(64):
        for j in range(64):
            s=""
            for k in range(8):
                s+=str(L[i][j][k])
            compressed.append((int(s,2)))
            f.write(chr((int(s,2))))
            s=""
            for k in range(8,16):
                s+=str(L[i][j][k])
            compressed.append((int(s,2)))
            f.write(chr((int(s,2))))
    print len(compressed)
    f.close()
def storeint(L,filename):
    f=open(filename+".dat",'w+b')
    try:
        for i in L:
            f.write(chr((int(i))))
    except:
        print 'larger than 256'
    f.close()
chdir('.')
imfile='lena.bmp'
if path.splitext(imfile)[1] != "jpg":
    outfile = path.splitext(imfile)[0] + ".jpg"
    try:
        Image.open(imfile).save(outfile)
        imfile=outfile
    except:
        print "Unable to write as 'jpeg'"
img=Image.open(imfile).convert('RGB')
img.show()
L=[[[]for i in range(64)] for j in range(64)]
for i in range(256):
    for j in range(256):
        L[int (i/4)][int(j/4)].append(img.getpixel((i,j)))
R=[[[L[i][j][k][0] for k in range(16) ]for i in range(64)] for j in range(64)]

G=[[[L[i][j][k][1] for k in range(16)]for i in range(64)] for j in range(64)]

B=[[[L[i][j][k][2] for k in range(16)]for i in range(64)] for j in range(64)]
R,Ralist,Rblist=compress(R)
G,Galist,Gblist=compress(G)
B,Balist,Bblist=compress(B)
storeint(Ralist,'ared')
storeint(Rblist,'bred')
storeint(Balist,'ablue')
storeint(Bblist,'bblue')
storeint(Galist,'agreen')
storeint(Gblist,'bgreen')
"""for i in range(64):
    for j in range(64):
        for k in range(16):
         #   print [R[i][j][k],G[i][j][k],B[i][j][k]]
            if k == 0:
                img.putpixel((i*4+int(k/4),j*4+k%4),((R[i][j][k]<<7)+(G[i][j][k]<<6)+(B[i][j][k]<<5),int(Ralist[i*64+j]),int(Rblist[i*64+j])))
            elif k == 1:
                img.putpixel((i*4+int(k/4),j*4+k%4),((R[i][j][k]<<7)+(G[i][j][k]<<6)+(B[i][j][k]<<5),int(Galist[i*64+j]),int(Gblist[i*64+j])))
            elif k == 2:
                img.putpixel((i*4+int(k/4),j*4+k%4),((R[i][j][k]<<7)+(G[i][j][k]<<6)+(B[i][j][k]<<5),int(Balist[i*64+j]),int(Bblist[i*64+j])))
            else:
                img.putpixel((i*4+int(k/4),j*4+k%4),((R[i][j][k]<<7)+(G[i][j][k]<<6)+(B[i][j][k]<<5),0,0))
img.save('compressed.gif')"""
store(R,'redlayer')
store(B,'bluelayer')
store(G,'greenlayer')
system("zip compressed.zip *.dat")
system("move compressed.zip C:\Users\FarhanK\Desktop\Project\Result")
