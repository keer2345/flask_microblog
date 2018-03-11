import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.sina.com.cn'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'keer2345'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '912229hui'
    ADMINS = ['keer2345@163.com']
    # ADMINS = ['admin@example.com']

    POSTS_PER_PAGE = 2
