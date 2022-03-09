from linecache import lazycache
import profile
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    prof_pic_path = db.column(db.String())
    pass_safe = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='user', lazy='dynamic')
    upvotes = db.relationship('UpVotes', backref='user', lazy='dynamic')
    downvotes = db.relationship('DownVotes', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_safe = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_safe,password)

    def user_save(self):
        db.session.add(self)
        db.session.commit()

    def user_delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class Pitches(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitchtitle = db.Column(db.String(255),nullable = False)
    pitch = db.Column(db.text(),nullable = False)
    comments = db.relationship('Commente', backref='ptch', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='pitch',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='pitch',lazy='dynamic')
    pitcher = db.column(db.Interger, db.Foreignkey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True,nullable = False)


    def pitch_save(self):
        db.session.add(self)
        db.session.commit()

    def pitch_delete(self):
        db.session.delete(self)
        db.session.commit()   

    def __repr__(self):
        return f'User {self.pitch}'

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'