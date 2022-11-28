"""
I wrote this code making some array progress until I know cv2.imencode() function.
This code is too slow. Dont use this code. Instead, use the other python script named imencode.
"""
import cv2
import numpy as np
import time

img= cv2.imread("resim/tfm.jpg")
img1= cv2.imread("resim/tfm.jpg")
print(type(img))
y, x = len(img), len(img[0])
print(y, x)
print(img)
for y1 in range(y):
    i=img[y1]
    print(y1)
    for x1 in range(x):
        data=i[x1]
        imgstr=np.array_str(data)
        #print(img)
        imgstr=imgstr.replace("[","")
        imgstr=imgstr.replace("]","")
        #print(img)
        """
        for a1 in range(3):
            img=i[a1]
            print(img)"""
        imgstr=np.fromstring(imgstr, dtype=int, sep=" ")
        #print(img)
        if x1==0:
            arr1=imgstr
        else:
            arr1=np.vstack((arr1, imgstr))
    if y1==0:
        arr2=arr1
    else:
        arr2=np.vstack((arr2, arr1))
#arr1=np.array(arr1)
print(img.shape, arr2.shape)
#time.sleep(100)
arr2=np.array(arr2.reshape(353,616,3), dtype=np.uint8)
print(arr2==img)
print(type(arr2), type(img))
print(img.shape, arr2.shape)

#print(img1)
cv2.imshow("hi",arr2)

