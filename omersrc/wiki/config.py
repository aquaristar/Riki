# encoding: utf-8

SECRET_KEY='a unique and long key'
TITLE='Riki' 
HISTORY_SHOW_MAX=30
PIC_BASE = '/static/content/'
CONTENT_DIR = 'content/'
NUMBER_OF_HISTORY = 5

SQLALCHEMY_DATABASE_URI = 'mysql://omer:wiki@127.0.0.1/wiki_db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True