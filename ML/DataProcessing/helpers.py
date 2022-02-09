import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from flask import flash
import shutil

def detectFaceAndCrop(image_name,save_dir):
    image = cv2.imread(image_name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_copy = np.copy(image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(gray_image, 1.25, 6)
  
    if (len(faces) > 0):
        for f in faces:
            x, y, w, h = [ v for v in f ]
            cv2.rectangle(image_copy, (x,y), (x+w, y+h), (255,0,0), 3)
            face_crop = gray_image[y:y+h, x:x+w] 
            im = Image.fromarray(face_crop)
            im.save(save_dir)
    return len(faces)


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
        
        
def create_labels(path):
    files = list_files(path)
    for i in files:
        with open(f'{path}/{i}/label', 'w') as f:
            f.write('1')
            f.close()

def find_crop_faces(path):
    count = 0
    dirs = list_files(path)
    create_prcessing_dirs(path)
    for i in dirs:
        if i == 'processed':
            continue
        images = list_files(f'{path}/{i}')
        for j in images:            
            return_code = detectFaceAndCrop(f'{path}/{i}/{j}',f'{path}/processed/{i}/{j}')
            count +=1
            if return_code == 0:
                break
            
    return return_code,count


def delete_all_files(path):
    files_in_notProcessed = list_files(path)
    if(len(files_in_notProcessed)>=1):
        for f in files_in_notProcessed:         
             os.remove(f'{path}/{f}')


def if_exists_detele(path):
    if os.path.exists(path):        
            shutil.rmtree(path)


# coding=utf-8 
# import Image
# import os.path
# import glob


# def jpg2pgm( jpg_file, pgm_dir ):
#     jpg = Image.open( jpg_file)
#     jpg = jpg.resize( (100,100), Image.BILINEAR)
#     name =(str)(os.path.join( pgm_dir, os.path.splitext( os.path.basename(jpg_file) )[0] ))+".pgm"
#     # Create target pgm file
#     jpg.save( name)

# for jpg_file in glob.glob("./*.jpg"):
#     jpg2pgm( jpg_file, "/home/sam/pgm/")


