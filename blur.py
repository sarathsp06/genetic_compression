#!/usr/bin/python
import sys, os
from PIL import Image
import cv2
import numpy as np
import sys

class image:
	def __init__(self,i,img):
		try:
			self.img  = cv2.imread(img)
			self.i = i
			self.tries = 0
			self.fn = {0:self.gaussian,1:self.bilateral,2:self.median}
		except Exception,e:
			print "Exception occured :",e.message
	def gaussian(self):
		self.img  = cv2.GaussianBlur(self.img,(i,i),0)
	def bilateral(self):
		slef.img  = cv2.bilateralFilter(self.img,i,i*2,i/2)
	def median(self):
		self.img = cv2.medianBlur(self.img,i)
	def sharpen(self):
		"""i will do it"""
		pass
	def save(self,outfile):
		cv2.imwrite(outfile,self.img)
	def check_psnr(self):
		"""Do it yourself and send me hope ypu got hat i meant"""
		pass
	def do(self,sequence):
		for i in range(3):
			self.fn[i]()
		self.sharpen()
		return self.check_psnr()

if __name__ == "__main__":
	inputFile = sys.argv[1]
	i = int(sys.argv[2])
	outputFile = "blur"+os.path.splitext(inputFile)[1]
	img = cv2.imread(inputFile)
	try:
		img = cv2.medianBlur(img,i)
		gaussian_blur  = cv2.GaussianBlur(img,(i*2+1,i*2+1),0)
		bilateral_blur = cv2.bilateralFilter(gaussian_blur,i*2,i*2,i*2)
	except Exception,e:
		print "Exception :",e.message
	try:
		img = cv2.cv.fromarray(bilateral_blur)
		cv2.cv.SaveImage("b"+outputFile,img)
		img = cv2.cv.fromarray(gaussian_blur)
		cv2.cv.SaveImage("g"+outputFile,img)
	except Exception,e:
		print "Exception While saving:",e.message


