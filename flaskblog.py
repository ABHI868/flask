


from flask import Flask,render_template, url_for,flash,redirect
from forms import LoginForm,RegistrationForm
app=Flask(__name__)
app.config['SECRET_KEY']='12345'
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
        form=RegistrationForm()
        if form.validate_on_submit():
            flash("Account was created for {}",form.username.data,'success')

            return redirect(url_for('home'))
        else:
            return render_template('registration.html', title="Register",form=form)



@app.route('/login',methods=['GET','POST'] )
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=="abc@zero.com" and form.password.data=="abc":
            flash("You have been logged in" ,'success')
            return redirect(url_for('home'))
        else:
            flash("Please check your credentials" ,'danger')
    return render_template('login.html', title="Login",form=form)
if __name__=="__main__":
    app.run(debug=True)