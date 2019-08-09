#! coding: utf-8
from flask_mongoengine import MongoEngine

from utils.factory import app


class Collection(object):

    @classmethod
    def init_collection(cls, app):
        db = MongoEngine()
        db.init_app(app)

        return db


db = Collection.init_collection(app)
