#reading image 
import cv2
img=cv2.imread("butterfly.jpg")
cv2.imshow("display image",img)
print(img)
greyimg=cv2.cvtColor(img,cv2.COLOR_RGB2GREY)
cv2.imshow("greyscale image",greyimg)
print(greyimg)
cv2.waitKey(0)
