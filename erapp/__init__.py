#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import app_config

# Main Application and Config
app = Flask('erapp')
app.config.from_object(app_config)

# Database initialization
db = SQLAlchemy(app=app)

def build_app():
    from erapp.controllers.index import index
    app.register_blueprint(index)
    return app

# if __name__ == '__main__':
#     app.run()
