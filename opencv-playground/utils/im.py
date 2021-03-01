import cv2
import matplotlib.pyplot as plt 
import numpy as np 

def show(image, axis='off'):
	img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	plt.imshow(img)
	plt.axis(axis)
	plt.show()