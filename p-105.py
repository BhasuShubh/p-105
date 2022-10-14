import cv2
import os

path ="Images"

images =[]

for file in os.listdir(path):
    name , ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        images.append(file_name)
        
count = len(images)

img =cv2.imread(images[0])
height , width, channels =img.shape
size =(width , height)

photos = cv2.VideoWriter("slideshow.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 1 , size)

for i in range(0, count , 1) :
    img = cv2.imread(images[i])
    photos.write(img)
photos.release()