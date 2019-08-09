#! coding: utf-8

import logging
from flask_restplus_patched import Namespace, abort
from flask_restplus import Resource

from simple.repository import test_result

simple_ns = Namespace('simple')
logger = logging.getLogger("simple")


class CurrentUserResource(Resource):

    def get(self):
        result = test_result()
        logger.info(result)
        if result:
            return {"data": result[0].id}
        else:
            return {"data": 0}
