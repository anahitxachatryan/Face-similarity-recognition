from flask import Blueprint,render_template, request
from flask_login import  login_required, current_user
import os 

views =  Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user = current_user)

@views.route('/uploadImg',methods = ['GET','POST'])
@login_required
def uploadImg():
    # check if files are uploaded
    # check to upload jpeg/png
    # if the imgs_for_model is not empty, remove all then save new files
    # when uploaded and stored, call crop and detect method
    # add loading bar when crop/detect the face
    # add a description -> need to upload an img where the face is ...
    if request.method == 'POST':
        file1 = request.files['img1']
        file2 = request.files['img2']
        file1.save(os.path.join('./imgs_for_model',file1.filename))
        file2.save(os.path.join('./imgs_for_model',file2.filename))
        # if file1.filename != '' & file2.filename != '':
        #     if len(os.listdir(path='./imgs_for_model')) == 0:
        #         
        #     else:
        #         import glob
        #         files = glob.glob('./imgs_for_model/*')
        #         for f in files:
        #             os.remove(f)
    return render_template('uploadImg.html', user = current_user)
