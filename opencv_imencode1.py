import cv2
import numpy as np
import time

img= cv2.imread("resim/tfm.jpg")

img=cv2.imencode(".jpg", img)[1]
print(img)
byte_img = img.tobytes()
print(len(byte_img))

recvd_img=np.array(bytearray(byte_img), dtype="uint8")
recvd_img=cv2.imdecode(recvd_img, cv2.IMREAD_COLOR)
cv2.imshow("sa", recvd_img)

