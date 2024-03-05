import cv2
import os
# current directory to fetch the images
x = os.getcwd()
os.chdir(x+'/Resources/newCap/geo')
# changes images name by geo
st = "geo"
lst = os.listdir(os.getcwd())
# itrearting images and renaming it
count = 1
for i in lst:
    os.renames(i,st+str(count)+".jpg")
    count+=1

lst2 = os.listdir(os.getcwd())
# in current directory cropping the images using OPENCV
for i in lst2:
    img = cv2.imread(i)
    imgCropped = img[612:758,15:1120]
    # resizing the images
    imgResize = cv2.resize(imgCropped,(900,100))
    cv2.imwrite(i,imgResize)
    # cv2.imshow('Cropped image', imgResize)
    # cv2.waitKey(0)



