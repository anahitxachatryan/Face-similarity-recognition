from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import User
from . import db

auth =  Blueprint('auth', __name__)


@auth.route('/login',methods = ['GET','POST'])
def login():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully.", category='success')
                return redirect(url_for('views.home'))
            else:
                flash("Password is not correct.", category='error')
        else:
            flash("Email does not exist.", category='error')
                
        
    
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
        user = User.query.filter_by(email=email).first()
        if user:
             flash("Email already exist, please use another email.", category='error')
        
        elif len(email) < 4 :
            flash("Email must be greater than 5 characters.", category="error")
        elif len(firstName) < 2:
            flash("Firstname must be greater than 3 characters.", category="error")
        elif len(password1) < 7:
            flash("Password must be greater than 8 characters.", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match.", category="error")
        
        else:
            password_hashed= generate_password_hash(password1,method='sha256')
            new_user = User(email = email, firstName = firstName, password = password_hashed)
            db.session.add(new_user)
            db.session.commit()
            
            flash("Account is created successfully.",category="success")
            return redirect(url_for('views.home'))
    
    return render_template('sign-up.html')
