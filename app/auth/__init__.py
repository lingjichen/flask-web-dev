from flask import Blueprint

#构造函数接受蓝本的名字和蓝本所在的包或模块
auth = Blueprint('auth', __name__)

#注册路由的程序在views中，错误处理程序在errors中，在末尾导入避免循环导入依赖
from . import views
