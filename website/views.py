from flask import Blueprint, redirect,render_template, request, flash, url_for
from flask_login import  login_required, current_user
import os

from ML.DataProcessing import helpers




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
        file_types = ['.jpeg','.jpg','.JPG','.JPEG','.png', '.pgm']
        name, extension = os.path.splitext(file1.filename)
        name2, extension2 = os.path.splitext(file2.filename)
        helpers.if_exists_detele('website/static/imgs_for_model/notProcessed/processed')
        helpers.delete_all_files('website/static/imgs_for_model/notProcessed/1')
        helpers.delete_all_files('website/static/imgs_for_model/notProcessed/2')
        if (extension in file_types) & (extension2 in file_types):

            file1.save(os.path.join('website/static/imgs_for_model/notProcessed/1/',file1.filename))
            file2.save(os.path.join('website/static/imgs_for_model/notProcessed/2/',file2.filename))
            return_code,count, encodings = helpers.find_crop_faces('website/static/imgs_for_model/notProcessed')

            if return_code == 0:
                flash(f"Face is not detected on image {count}", category='error')
                helpers.delete_all_files('website/static/imgs_for_model/notProcessed/1')
                helpers.delete_all_files('website/static/imgs_for_model/notProcessed/2')
                helpers.if_exists_detele('website/static/imgs_for_model/notProcessed/processed')
            else:
                img1 = helpers.list_files('website/static/imgs_for_model/notProcessed/processed/1')
                img2 = helpers.list_files('website/static/imgs_for_model/notProcessed/processed/2')
                results = helpers.calculate_results(encodings[0],encodings[1])


                return redirect(url_for('views.see_result',img1 = img1[0],img2=img2[0], results = results))

        else:
            flash("Please upload .jpeg, .jpg or .png files", category='error')

    return render_template('uploadImg.html', user = current_user)


@views.route('/face_rec',methods = ['GET','POST'])
@login_required
def see_result():
    img1 = request.args.get('img1')
    img2 = request.args.get('img2')
    results = request.args.get('results')

    return render_template('faceRecognition.html', user = current_user,img1=img1, img2=img2,
    result_distance=results)