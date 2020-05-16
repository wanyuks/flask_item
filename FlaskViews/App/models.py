from werkzeug.security import check_password_hash, generate_password_hash

from App.ext import db


class Students(db.Model):
    s_id = db.Column(db.Integer, primary_key=True)
    s_job_id = db.Column(db.String(32), unique=True)
    # _s_password = db.Column(db.String(256))
    # s_phone = db.Column(db.String(32), nullable=False, unique=True)

    @property
    def s_password(self):
        raise Exception("Error Action: Password can not be access")

    @s_password.setter
    def s_password(self, value):
        self._s_password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self._s_password, password)


class User(db.Model):
    # 修改表名
    # __tablename__ = "users_new"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    description = db.Column(db.String(128), nullable=True)

