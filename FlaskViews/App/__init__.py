from flask import Flask

from App.settings import envs
from App.views import init_blue
from App.ext import init_ext
from middlewares.middleware import load_middleware


def create_app(env):
    app = Flask(__name__)
    # 初始化参数
    app.config.from_object(envs.get(env))
    # 初始化第三方库
    init_ext(app)
    # 初始化路由
    init_blue(app)

    load_middleware(app)
    return app
