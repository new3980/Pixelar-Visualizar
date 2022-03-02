#This file is created to obsereve the differences between each interpolation technique
#2 Subjects will be used which are
# -Zutomayo pic (img)   | - N pic (letter)

"""
INTER_NEAREST - a nearest-neighbor interpolation
INTER_LINEAR - a bilinear interpolation (used by default)
INTER_AREA - resampling using pixel area relation. It may be a preferred method for image decimation, 
            as it gives moire’-free results. But when the image is zoomed, it is similar to theINTER_NEAREST method.
INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood
INTER_LANCZOS4 - a Lanczos interpolation over 8x8 pixel neighborhood
"""
import cv2
import matplotlib.pyplot as plt

zutomayo = "D:\\GIT\\Pixelar-Visualizar\\cv2-interpolate\\zutomayo.jpg"
num18 = "D:\\GIT\\Pixelar-Visualizar\\cv2-interpolate\\18.jpg"

img = cv2.imread(zutomayo)
imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
letter = cv2.imread(num18)

#Original image dimension is 360x360px both
#Reduced to 120x120 px usign cv2.resize


#INTER_LINEAR
imgreduce1 = cv2.resize(imgrgb,(120,120),interpolation=cv2.INTER_LINEAR)
letterreduce1 = cv2.resize(letter,(120,120),interpolation=cv2.INTER_LINEAR)
imglarge1 = cv2.resize(imgrgb,(720,720),interpolation=cv2.INTER_LINEAR)
letterlarge1 = cv2.resize(letter,(720,720),interpolation=cv2.INTER_LINEAR)

print("LINEAR")
plt.subplot(3,2,1)
plt.imshow(imgrgb), plt.title("Original")
plt.subplot(3,2,2)
plt.imshow(letter), plt.title("Original")
plt.subplot(3,2,3)
plt.imshow(imgreduce1), plt.title("Reduce")
plt.subplot(3,2,4)
plt.imshow(letterreduce1), plt.title("Reduce")
plt.subplot(3,2,5)
plt.imshow(imglarge1), plt.title("Large")
plt.subplot(3,2,6)
plt.imshow(letterlarge1), plt.title("Large")
plt.show()

#INTER_AREA
imgreduce2 = cv2.resize(imgrgb,(120,120),interpolation=cv2.INTER_AREA)
letterreduce2 = cv2.resize(letter,(120,120),interpolation=cv2.INTER_AREA)
imglarge2 = cv2.resize(imgrgb,(720,720),interpolation=cv2.INTER_AREA)
letterlarge2 = cv2.resize(letter,(720,720),interpolation=cv2.INTER_AREA)

print("AREA")
plt.subplot(3,2,1)
plt.imshow(imgrgb), plt.title("Original")
plt.subplot(3,2,2)
plt.imshow(letter), plt.title("Original")
plt.subplot(3,2,3)
plt.imshow(imgreduce2), plt.title("Reduce")
plt.subplot(3,2,4)
plt.imshow(letterreduce2), plt.title("Reduce")
plt.subplot(3,2,5)
plt.imshow(imglarge2), plt.title("Large")
plt.subplot(3,2,6)
plt.imshow(letterlarge2), plt.title("Large")
plt.show()

#INTER_CUBIC
imgreduce3 = cv2.resize(imgrgb,(120,120),interpolation=cv2.INTER_CUBIC)
letterreduce3 = cv2.resize(letter,(120,120),interpolation=cv2.INTER_CUBIC)
imglarge3 = cv2.resize(imgrgb,(720,720),interpolation=cv2.INTER_CUBIC)
letterlarge3 = cv2.resize(letter,(720,720),interpolation=cv2.INTER_CUBIC)

print("CUBIC")
plt.subplot(3,2,1)
plt.imshow(imgrgb), plt.title("Original")
plt.subplot(3,2,2)
plt.imshow(letter), plt.title("Original")
plt.subplot(3,2,3)
plt.imshow(imgreduce3), plt.title("Reduce")
plt.subplot(3,2,4)
plt.imshow(letterreduce3), plt.title("Reduce")
plt.subplot(3,2,5)
plt.imshow(imglarge3), plt.title("Large")
plt.subplot(3,2,6)
plt.imshow(letterlarge3), plt.title("Large")
plt.show()

#INTER_CUBIC
imgreduce4 = cv2.resize(imgrgb,(120,120),interpolation=cv2.INTER_LANCZOS4)
letterreduce4 = cv2.resize(letter,(120,120),interpolation=cv2.INTER_LANCZOS4)
imglarge4 = cv2.resize(imgrgb,(720,720),interpolation=cv2.INTER_LANCZOS4)
letterlarge4 = cv2.resize(letter,(720,720),interpolation=cv2.INTER_LANCZOS4)

print("LANCZOS4")
plt.subplot(3,2,1)
plt.imshow(imgrgb), plt.title("Original")
plt.subplot(3,2,2)
plt.imshow(letter), plt.title("Original")
plt.subplot(3,2,3)
plt.imshow(imgreduce4), plt.title("Reduce")
plt.subplot(3,2,4)
plt.imshow(letterreduce4), plt.title("Reduce")
plt.subplot(3,2,5)
plt.imshow(imglarge4), plt.title("Large")
plt.subplot(3,2,6)
plt.imshow(letterlarge4), plt.title("Large")
plt.show()

#INTER_CUBIC
imgreduce5 = cv2.resize(imgrgb,(120,120),interpolation=cv2.INTER_NEAREST)
letterreduce5 = cv2.resize(letter,(120,120),interpolation=cv2.INTER_NEAREST)
imglarge5 = cv2.resize(imgrgb,(720,720),interpolation=cv2.INTER_NEAREST)
letterlarge5 = cv2.resize(letter,(720,720),interpolation=cv2.INTER_NEAREST)

print("NEAREST")
plt.subplot(3,2,1)
plt.imshow(imgrgb), plt.title("Original")
plt.subplot(3,2,2)
plt.imshow(letter), plt.title("Original")
plt.subplot(3,2,3)
plt.imshow(imgreduce5), plt.title("Reduce")
plt.subplot(3,2,4)
plt.imshow(letterreduce5), plt.title("Reduce")
plt.subplot(3,2,5)
plt.imshow(imglarge5), plt.title("Large")
plt.subplot(3,2,6)
plt.imshow(letterlarge5), plt.title("Large")
plt.show()