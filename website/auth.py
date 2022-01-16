import re
from flask import Blueprint,render_template,request,flash

auth =  Blueprint('auth', __name__)


@auth.route('/login',methods = ['GET','POST'])
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>logout</p>" 

@auth.route('/signup',methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4 :
            flash("email must be greater than 5 characters", category="error")
        elif len(firstName) < 2:
            flash("firstname must be greater than 3 characters", category="error")
        elif len(password1) < 7:
            flash("password must be greater than 8 characters", category="error")
        elif password1 != password2:
            flash("passwords don\'t match", category="error")
        
        else:
            flash("account is created successfully!",category="success")
    
    return render_template('sign-up.html')
