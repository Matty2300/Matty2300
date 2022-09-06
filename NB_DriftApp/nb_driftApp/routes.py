from nb_driftApp import app, bcrypt
from nb_driftApp.forms import loginForm, registerForm, postForm
from nb_driftApp.models import User, Post
from nb_driftApp.database import db_session
from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, current_user, logout_user,login_required




@app.route('/')
@app.route('/home', methods=['POST','GET'])
def home():
    posts = db_session.query(Post).all()
    
    return render_template('home.html', posts=posts)

@app.route('/backend', methods=['POST','GET'])
@login_required
def backend():
    form = postForm()
    if form.validate_on_submit():
        post = Post(headline=form.headline.data, msg_content=form.msg_content.data, expiration_date=form.expiration_date.data, author=current_user.username)
        db_session.add(post)
        db_session.commit()
        flash('Message has been posted','success')
        return redirect(url_for('backend'))
            
    return render_template('backend.html', form=form )

'''Login'''
# tester@brock.dk
# test

# testen@brock.dk
# test123

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('backend'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() #checking if the email exist in database, and return the first one
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)#check button for remember login
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('backend')) #loggin in user
        else:
            flash('Login Unsuccessful, Please check username and password','danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/home/register', methods=['GET','POST'])
def register():
    form = registerForm() # using registrationForm from forms.py class
    if form.validate_on_submit():
        space = ''
        uname = form.fornavn.data + space + form.efternavn.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #incrypting password made by user in register form
        user = User(email=form.email.data, password=hashed_password,fornavn=form.fornavn.data,efternavn=form.efternavn.data,username=uname) #storing users input in register fields
        db_session.add(user) #adding user to database
        db_session.commit() #committing to the changes
        flash('User has been added','success') #checking if form validate and register then shows message using "f" string and passing in username from forms.py, Bootstrap is passed in, to show "success"
        return redirect(url_for('backend'))# redirecting using the function of the page not the url '/home'
    return render_template('register.html', title='Register user', form=form) #passing in title and forms from forms.py classes for acces on the html page


@app.route('/home/<int:post_id>/delete', methods=['POST','GET'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if current_user.is_authenticated:
        db_session.delete(post)
        db_session.commit()
        flash('Post has been deleted','success')
        return redirect(url_for('home'))
    return redirect(url_for('home'))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

'''
@app.route('/datechecker', methods=['GET','POST'])
def datechecker():
    today = datetime.now().date()
    #query = db_session.query(Post.expiration_date).all()
    print(today)   
    for exDate in db_session.query(Post.expiration_date).all():
        if exDate <= today:
            print(f'exDate is TODAY {exDate}')
        else:
            pass
'''
       

 






