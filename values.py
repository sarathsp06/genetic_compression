from os import system 
from PIL import Image
from os import chdir,path
import math
#chdir('.')
imfile='C:\Users\FarhanK\Desktop\Project\Project\image\lenagray.bmp'
imfile1='C:\Users\FarhanK\Desktop\graylena.bmp'
img=Image.open(imfile).convert('RGB')
imgd=Image.open(imfile1).convert('RGB')
#imgd.show()
red=[]
blue=[]
green=[]
for i in range (256):
    for j in range (256):
        red.append(img.getpixel((i,j))[0])
        blue.append(img.getpixel((i,j))[2])
        green.append(img.getpixel((i,j))[1])
        #print red,blue,green
red1=[]
blue1=[]
green1=[]
for i in range (256):
    for j in range (256):
        red1.append(imgd.getpixel((i,j))[0])
        blue1.append(imgd.getpixel((i,j))[2])
        green1.append(imgd.getpixel((i,j))[1])
maxr=max(red)
maxb=max(blue)
maxg=max(green)
print red[0]
for i in range(65536):
    red[i]=red[i]-red1[i]
    blue[i]=blue[i]-blue1[i]
    green[i]=green[i]-green1[i]
print red[0]
for i in range (65536):
    red1[i]=abs(red[i])
    blue1[i]=abs(blue[i])
    green1[i]=abs(green[i])
#for i in range(65536):
 #   print red1[i]
sum4=sum5=sum6=0
for i in range(65536):
    sum4=sum4+red1[i]
    sum5=sum5+blue1[i]
    sum6=sum6+green1[i]
sum4=sum4/65536
sum5=sum5/65536
sum6=sum6/65536
print sum4,sum5,sum6
print 'MAE = ',(sum4+sum5+sum6)/3
sum1=sum2=sum3=0
for i in range(65536):
    sum1=sum1+(red[i]*red[i])
    sum2=sum2+(blue[i]*blue[i])
    sum3=sum3+(green[i]*green[i])
print sum1,sum2,sum3
sum1=sum1/65536
sum2=sum2/65536
sum3=sum3/65536
mse=sum1+sum2+sum3
mse=mse/3


psnr=(10*math.log10((maxr*maxr/mse))+10*math.log10((maxb*maxb/mse))+10*math.log10((maxg*maxg/mse)))/3
mse=math.sqrt(mse)
print 'MSE = ',mse
print 'PSNR =',psnr
mse=math.sqrt(mse)
#print 'RMSE =',mse
"""
i got the PSNR for the decompressed image dlena.bmp as 29.002
After applying genetic algorithm this value should get incresed i.e 30 or 31 etc
psnr of a layer = 10*log to the base 10((max pixel value of a layer)^2 /mse )
"""
