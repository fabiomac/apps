#--* coding: utf-8 *--#
import  os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:////home/fabiomac/aula_flask/storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'server##avna'