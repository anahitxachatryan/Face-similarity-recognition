import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def detectFaceAndCrop(image_name,save_dir):
  # Load in color image for face detection
  image = cv2.imread(image_name)

  # Convert the image to RGB colorspace
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  # Make a copy of the original image to draw face detections on
  image_copy = np.copy(image)

  # Convert the image to gray 
  gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    
  # Detect faces in the image using pre-trained face dectector
  faces = face_cascade.detectMultiScale(gray_image, 1.25, 6)

  # Print number of faces found
  if(len(faces) == 0):
    print(f'{image_name}')
    print('Number of faces detected:', len(faces))

  # Get the bounding box for each detected face
  for f in faces:
      x, y, w, h = [ v for v in f ]
      cv2.rectangle(image_copy, (x,y), (x+w, y+h), (255,0,0), 3)
      # Define the region of interest in the image  
      face_crop = gray_image[y:y+h, x:x+w]


  im = Image.fromarray(face_crop)
  im.save(save_dir)

def list_files(path):
    dir_list = os.listdir(path)
    if '.DS_Store' in dir_list:
        dir_list.remove('.DS_Store')
    return dir_list

def create_prcessing_dirs(path):
    files = list_files(path)
    if os.path.exists(f"{path}/processed"):
        print("processing path exists!") 
    else:
        os.mkdir(f"{path}/processed")
        for i in files:
            os.mkdir(f"{path}/processed/{i}")
        print("Directories are created")

def main():
    path = "needToProcess"
    dirs = list_files(path)
    create_prcessing_dirs(path)
    for i in dirs:
        if i == 'processed':
            continue
        images = list_files(f'{path}/{i}')
        for j in images:
            detectFaceAndCrop(f'{path}/{i}/{j}',f'{path}/processed/{i}/{j}')




main()