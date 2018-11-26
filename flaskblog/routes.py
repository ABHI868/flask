

from flaskblog.models import User,Post
from flask import render_template, url_for,flash,redirect,request
from flaskblog import app,bcrypt,db
from flaskblog.forms import LoginForm,  RegistrationForm
from flask_login import login_user,current_user,logout_user,login_required


@app.route("/")
@app.route("/home")
def home():

    blogs=[
        {
        'author': "Amit",
        'title':"How to use angular",
        "content":"First post content",
        "date":"20th Jan, 2017"},
        
        {
        'author':  "Ashok",
        "title": "How to use Data science",
        "content": "second post content",
        "date": "16th Feb, 2017"},
        
    ]
    return render_template("home.html" ,blogs=blogs)
@app.route("/about")
def about():
    return render_template("about.html",title="Flaskblog-About")


@app.route('/register' ,methods=['GET','POST'])
def register():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form=RegistrationForm()
        if form.validate_on_submit():
            # flash("Account was created for %s" %(form.username.data),'success') 
            hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user=User(username=form.username.data,email=form.email.data,password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash("Your account has been created! Please login with to continue" .format(form.username.data),'success') 
            return redirect(url_for('login '))


          

        else:
            return render_template('registration.html', title="Register",form=form)



@app.route('/login',methods=['GET','POST'] )
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            user_req=request.args.get('next')
            return redirect(user_req) if user_req else redirect(url_for('home'))
        
        else:
            flash("Please check your credentials" ,'danger')
    return render_template('login.html', title="Login",form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template("account.html" ,title="Account")