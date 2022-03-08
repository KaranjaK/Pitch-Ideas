from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_safe = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_safe = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_safe,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitches(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch = db.Column(db.String)
    pitcher = db.column(db.String)

    def __repr__(self):
        return f'User {self.pitch}'

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'