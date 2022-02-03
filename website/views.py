from flask import Blueprint,render_template, request
from flask_login import  login_required, current_user
import os 
from Data_process import detect_crop

views =  Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user = current_user)

@views.route('/uploadImg',methods = ['GET','POST'])
@login_required
def uploadImg():
    # check if files are uploaded +
    # if the imgs_for_model is not empty, remove all then save new files +
    # add a description -> need to upload an img where the face is ... +
    # check to upload jpeg/png
    # check if uploaded 2 images, otherwise flash error 
    # when uploaded and stored, call crop and detect method +
    # flask error if face is not detected
    # otherwise show the faces cropped
    # add loading bar when crop/detect the face
    # add the model
    if request.method == 'POST':
        file1 = request.files['img1']
        file2 = request.files['img2']
        
        
        files = detect_crop.list_files('imgs_for_model/notProcessed')
        if(len(files)>=2):
            for f in files:         
                os.remove(f'./imgs_for_model/notProcessed/{f}')
        file1.save(os.path.join('./imgs_for_model/notProcessed/',file1.filename))
        file2.save(os.path.join('./imgs_for_model/notProcessed/',file2.filename))
        detect_crop.find_crop_faces('imgs_for_model')

    return render_template('uploadImg.html', user = current_user)
