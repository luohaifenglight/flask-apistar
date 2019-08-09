#! coding: utf-8

from flask import Blueprint
from flask_restplus import Api, apidoc

from clannad.urls import routes, blueprints

# register center


class RegisterCenter(object):

    @classmethod
    def register_views(cls, app, name):
        api = Api(app)
        current_routes = routes.get(name, [])

        for child in current_routes:
            p_route, ns, children = child
            cls._register_chile_route(ns, children)
            api.add_namespace(ns, p_route)

    @classmethod
    def _register_chile_route(cls, ns, current):
        for child in current:
            ns.add_resource(child[1], child[0])

    @classmethod
    def create_blueprint(cls, name):
        """
        register blueprint
        """

        bp_v1 = Blueprint(name, __name__)
        cls.register_views(bp_v1, name)

        return bp_v1

    @classmethod
    def register_blueprints(cls, app):
        # params: app version
        # 注册版本
        for blueprint in blueprints:
            app.register_blueprint(cls.create_blueprint(blueprint[1]),
                                   url_prefix=blueprint[0])
