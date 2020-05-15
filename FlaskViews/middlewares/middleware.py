from flask import request


def load_middleware(app):
    @app.before_request
    def before():
        print("中间件：", request.url)
        """
            在这一块可以处理：
                统计
                优先级
                反爬
                    频率
                用户认证
                用户权限
        """
