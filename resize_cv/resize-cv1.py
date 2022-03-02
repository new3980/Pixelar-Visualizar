#syntax is cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
#see https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/

#src = [required] source/input image
#dsize = [required] desired size for the output image
#fx = [optional] scale factor along the horizontal axis
#fy = [optional] scale factor along the vertical axis
#interpolation = [optional] flag that takes one of the following methods. 
                 #INTER_NEAREST – a nearest-neighbor interpolation INTER_LINEAR 
                 # – a bilinear interpolation (used by default) INTER_AREA – 
                 # resampling using pixel area relation. It may be a preferred 
                 # method for image decimation, as it gives moire’-free results. 
                 # But when the image is zoomed, it is similar to the INTER_NEAREST method. 
                 # INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood 
                 # INTER_LANCZOS4 – a Lanczos interpolation over 8×8 pixel neighborhood

#Resize operations
import cv2
import matplotlib.pyplot as plt
path = "D:\\GIT\\Pixelar-Visualizar\\resize_cv\\asuka.jpg"



#1.Resize & Preserve aspect ratio
img = cv2.imread(path) # unchanged
imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print("Original :",img.shape) 
#Result = 836,836
#img.shape = [y,x] 2 variable 
"""
Want 80% scale
"""
scale = 80
width = int(img.shape[1]*(scale/100))
height = int(img.shape[0]*(scale/100))
dimension = (width,height)

res1 = cv2.resize(img,dimension,interpolation = cv2.INTER_AREA)
res1rgb = cv2.cvtColor(res1,cv2.COLOR_BGR2RGB)
#print("Resized :",res1.shape)
#Result = 668,668 y,x
plt.subplot(1,2,1)
plt.imshow(imgrgb)
plt.subplot(1,2,2)
plt.imshow(res1rgb)
plt.show()

