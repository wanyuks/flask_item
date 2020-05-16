# coding: utf-8


def get_db_uri(db_info):
    # uri: 数据库+驱动://username:password@host:port/具体哪一个库
    engine = db_info.get("ENGINE", "sqlite")
    device = db_info.get("DEVICE", "sqlite")
    username = db_info.get("USERNAME", "")
    password = db_info.get("PASSWORD", "")
    host = db_info.get("HOST", "localhost")
    port = db_info.get("PORT", 3306)
    database = db_info.get("DATABASE", "test")
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, device, username, password, host, port, database)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "wanyuks"
    # SESSION_TYPE = "redis"


# 开发环境的配置
# 可根据不同的环境要求配置不同的参数，如配置测试环境，演示环境
class DevelopmentConfig(Config):
    DEBUG = True
    db_info = {
        "ENGINE": "mysql",
        "DEVICE": "pymysql",
        "USERNAME": "root",
        "PASSWORD": "123456",
        "HOST": "10.57.20.154",
        "PORT": 3307,
        "DATABASE": "fit"
    }

    # MAIL_SERVER = 'smtp.163.com'
    # MAIL_PORT = 25
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = "wangwanyuks@163.com"
    # MAIL_PASSWORD = "wanyuks4626417"
    # MAIL_DEFAULT_SENDER = MAIL_USERNAME

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


envs = {
    "develop_config": DevelopmentConfig
}
