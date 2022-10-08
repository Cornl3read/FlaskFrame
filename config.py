import os


class Configs(object):
    TESTING = False
    DEBUG = False
    # Using a basic secret and salt for Stream !!!!! Change these values !!!
    SECRET_KEY = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')
    SECURITY_FLASH_MESSAGES = True


class ProductionConf(Configs):
    DATABASE_URI = ""
    SECURITY_EMAIL_SENDER = ''


class DevConf(Configs):
    DATABASE_URI = "sqlite:///tmp/the_test.db"
    DEBUG = True
    SECURITY_REGISTERABLE = True
    SECURITY_DEFAULT_REMEMBER_ME = True
    SECURITY_LOGIN_URL = '/get_it'
    SECURITY_LOGOUT_URL = '/get_lost'
    SECURITY_LOGOUT_METHODS = ["GET", "POST"]
    SECURITY_POST_LOGIN_VIEW = "/home"
    SECURITY_POST_LOGOUT_VIEW = "/"
    SECURITY_UNAUTHORIZED_VIEW = "None"
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_POST_REGISTER_VIEW = "/login"
    SECURITY_USERNAME_ENABLE = False
    SECURITY_CONFIRMABLE = False
    SECURITY_CHANGEABLE = True
    SECURITY_CHANGE_URL = "/change"
    SECURITY_POST_CHANGE_VIEW = "/login"
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    SECURITY_SEND_PASSWORD_RESET_EMAIL = False
    SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = False
    SECURITY_TRACKABLE = True


class TestConf(Configs):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True

