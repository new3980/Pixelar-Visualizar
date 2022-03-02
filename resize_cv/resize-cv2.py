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

#2. Resize & don't preserve aspect ration
img = cv2.imread(path)
imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#Define desired width or height
width1 = 500
height1 = 500
width = img.shape[1] #original
height = img.shape[0] #original 

dim1 = (width,height1)
dim2 = (width1,height)

res1 = cv2.resize(img,dim1,interpolation = cv2.INTER_AREA)
res2 = cv2.resize(img,dim2,interpolation = cv2.INTER_AREA)

res1rgb = cv2.cvtColor(res1,cv2.COLOR_BGR2RGB)
res2rgb = cv2.cvtColor(res2,cv2.COLOR_BGR2RGB)

print("Resized height:",res1.shape)
print("Resized width:",res2.shape)

plt.subplot(1,3,1)
plt.imshow(imgrgb)
plt.subplot(1,3,2)
plt.imshow(res1rgb)
plt.subplot(1,3,3)
plt.imshow(res2rgb)
plt.show()

#3. is just resize to desired size with both width and height changed so I will not do cause I'm lazy haha
