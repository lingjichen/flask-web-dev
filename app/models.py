from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))#密码散列值

    @property
    def password(self):
        raise AttributeError('密码不是可读的属性')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)#赋值password_hash

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)#验证密码

    def __repr__(self):
        return '<User %r>' % self.username