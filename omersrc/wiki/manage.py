import os
import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from wiki.web import create_app, db
from wiki.web import models

directory = os.getcwd()
directory = os.path.abspath(click.format_filename(directory))

app = create_app(directory)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()