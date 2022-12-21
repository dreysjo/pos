import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/shop_invoice'
    SQLALCHEMY_TRACK_MODIFICATIONS = False