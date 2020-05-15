import random

from flask import Blueprint, request, render_template
from flask import Response, session, redirect, url_for, flash
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

from .ext import db, mail
from .models import Students

blue = Blueprint("blue", __name__)


def init_blue(app):
    app.register_blueprint(blue)


@blue.route("/")
def index():
    return "index"


@blue.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        response = Response("登陆成功%s" % username)
        # response.set_cookie(key="username", value=username)
        session['username'] = username
        return response


@blue.route("/mine/", methods=["GET", "POST"])
def mine():
    # username = request.cookies.get("username")
    username = session.get("username")
    return "欢迎回来%s" % username


# @blue.route("/students/")
# def students():
#     student_list = ["小明 %s" % i for i in range(10)]
#     return render_template("students.html", student_list=student_list)


@blue.route("/addstudent/")
def add_students():
    # 创建一个sutdent的实例
    students = Students()
    students.name = "小花%d" % random.randint(100, 1000)
    # 使用数据库的会话添加数据并保存
    db.session.add(students)
    db.session.commit()
    print(db.session)
    print(type(db.session))
    return "Add Success"


@blue.route("/getstudent/")
def get_student():
    student = Students.query.first()
    return student.name


@blue.route("/student/register/", methods=["GET", "POST"])
def student_register():
    if request.method == "GET":
        return render_template("StudentsRegister.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # hash_pwd = generate_password_hash(password)
        student = Students()
        student.s_name = username
        student.s_password = password
        db.session.add(student)
        db.session.commit()
        return "Register Success"


@blue.route("/student/login/", methods=["GET", "POST"])
def student_login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        student = Students.query.filter(Students.s_name.__eq__(username)).first()
        if student and student.check_password(password):
            return "Login Success"
        flash("用户名或密码错误")
        return redirect(url_for("blue.student_login"))


@blue.route("/sendmail/")
def send_mail():
    msg = Message("Flask Email", recipients=['694846404@qq.com'])
    msg.body = "flask的一个邮件测试"
    msg.html = "<h2>Flask Email Test</h2>"
    mail.send(msg)
    return "邮件发送成功！！！"


@blue.route("/sendphone/")
def send_phone():

    return "发送成功"
