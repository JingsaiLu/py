CSFR_ENABLED = True
SECRET_KEY = 'flask'

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_blog.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')