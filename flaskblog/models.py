

from flaskblog import db,login_manager
from datetime import datetime

from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    username =db.Column(db.String(20), unique=True, nullable=False)
    email =db.Column(db.String(50), unique=True, nullable=False)
    password =db.Column(db.String(20), nullable=False)
    id =db.Column(db.Integer,primary_key=True)
    image_file =db.Column(db.String(20),default="default.jpeg",nullable=False)
    posts =db.relationship('Post',backref="author",lazy=True)

    def __repr__(self):
        return ("User {}{}{}" .format("{self.username}","{self.password}",'{self.image_file}'))

class Post(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(60),nullable=False)
    content=db.Column(db.Text(160),nullable=False)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)


    def __repr__(self):
        return ("Post {}{}" .format(self.title,self.date))