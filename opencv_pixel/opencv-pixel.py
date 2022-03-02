#Using opencv to make pixelart image (I think this would be better for objects)
#import skimage
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:\\GIT\\Pixelar-Visualizar\\opencv_pixel\\cassette.jpg")
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


plt.subplot(1,2,1)
plt.imshow(img) #BGR version
plt.subplot(1,2,2)
plt.imshow(rgb) #RGB version
plt.show() 

#Use open cv resize function by shrinking then resize again to original size see 'resize-cv.py'

