import os
import cv2
import shutil
import face_recognition as face_rec

def detectFaceAndCrop(image_name,save_dir):

    img = face_rec.load_image_file(image_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faceLocation = face_rec.face_locations(img)[0]
    encode_img= face_rec.face_encodings(img)[0]
    top_left_x = faceLocation[3]
    top_left_y = faceLocation[0]
    bot_right_x = faceLocation[1]
    bot_right_y = faceLocation[2]
    img = img[top_left_y:bot_right_y, top_left_x:bot_right_x]
    cv2.imwrite(save_dir, img)
    return len(face_rec.face_locations(img)), encode_img

def calculate_results(encodedImg1, encodedImg2):

    return face_rec.compare_faces([encodedImg1], encodedImg2)


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


def find_crop_faces(path):
    count = 0
    dirs = list_files(path)
    create_prcessing_dirs(path)
    encodings = []
    for i in dirs:
        if i == 'processed':
            continue
        images = list_files(f'{path}/{i}')
        for j in images:
            return_code, encodedImg = detectFaceAndCrop(f'{path}/{i}/{j}',f'{path}/processed/{i}/{j}')


            count +=1
            if return_code == 0:
                break

        encodings.append(encodedImg)

    return return_code, count, encodings


def delete_all_files(path):
    files_in_notProcessed = list_files(path)
    if(len(files_in_notProcessed)>=1):
        for f in files_in_notProcessed:
             os.remove(f'{path}/{f}')


def if_exists_detele(path):
    if os.path.exists(path):
            shutil.rmtree(path)




