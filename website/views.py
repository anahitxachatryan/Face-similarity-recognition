from flask import Blueprint,render_template, request, flash
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
    
    if request.method == 'POST':
        file1 = request.files['img1']
        file2 = request.files['img2']
        file_types = ['.jpeg','.jpg','.png']
        name, extension = os.path.splitext(file1.filename)
        name2, extension2 = os.path.splitext(file2.filename)
        detect_crop.if_exists_detele('imgs_for_model/processed')
        detect_crop.delete_all_files('imgs_for_model/notProcessed')
        if (extension in file_types) & (extension2 in file_types):           
            
            file1.save(os.path.join('./imgs_for_model/notProcessed/',file1.filename))
            file2.save(os.path.join('./imgs_for_model/notProcessed/',file2.filename))
            return_code,count = detect_crop.find_crop_faces('imgs_for_model')
            if return_code == 0:
                flash(f"Face is not detected on image {count}", category='error')
                detect_crop.delete_all_files('imgs_for_model/notProcessed')
                detect_crop.if_exists_detele('imgs_for_model/processed')              
            
        else:
            flash("Please upload .jpeg, .jpg or .png files", category='error')
    return render_template('uploadImg.html', user = current_user)
