from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from hashlib import md5
# from time import time
# import jwt
# from app import create_app


class User(UserMixin, db.Model):
    '''
    UserMixin class includes generic implementations appropriate for most user model classes
    '''
    __tablename__ = 'users'
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique = True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(130))
    pitch = db.relationship('Pitch', backref='author', lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comments', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

        #user object does secured password verification



    def __repr__(self):
        return '{}'.format(self.username)

    '''
    Flask-login keeps track of the logged in
    user by storing its unique identifier in Flask's
    user session.
    '''

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user(cls, id):
<<<<<<< HEAD
        users = User.query.filter_by(user_id = id).all()
=======
        users = User.query.filter_by(User.id = id).all()
>>>>>>> 0d40a78dc1505fb4a4dcabc5ff2491f48afa6777
        return users


class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    category = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @classmethod
    def retrieve_posts(cls, id):
<<<<<<< HEAD
        pitch = Pitch.filter_by(id=id).all()
=======
        pitch = Pitch.query.filter_by(id=id).all()
>>>>>>> 0d40a78dc1505fb4a4dcabc5ff2491f48afa6777
        return pitch

    '''
    Pitch class represent the pitches Pitched by
    users. Timestamp is set to default and passsed datetime.utcnow--> function.
    SQLAlchemy will set the field to the value of calling that function
    and not the result of calling it without ()
    The user_id field is initialized as a foreign key to user.id,
    which means that it references an id value from the users table
    '''

    def __repr__(self):
        return '{}'.format(self.body)


class Comments(db.Model):
<<<<<<< HEAD

=======
>>>>>>> 0d40a78dc1505fb4a4dcabc5ff2491f48afa6777
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
