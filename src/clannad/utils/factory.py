#! coding: utf-8

from flask import Flask
import logging


class Factory(object):

    @classmethod
    def create_app(cls):
        app = Flask(__name__)
        app.config.from_object('clannad.settings')
        app.logger.setLevel(logging.INFO)
        return app

app = Factory.create_app()
