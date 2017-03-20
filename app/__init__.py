from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.session_protection = 'strong'#session_protection提供不同安全等级防止用户会话遭篡改
login_manager.login_view = 'auth.login'


#创建程序工厂，接受配置名
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

#从main文件夹中提供模块，注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

#从auth文件夹中提供模块，注册蓝本,url_prefix为可选参数，为蓝本注册的所有路由加上指定前缀'/auth'
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

#从api中提供模块
    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')


    return app
