# coding: utf-8

import os
import random
from mongoengine.connection import uri_parser


MONGODB_SETTINGS = {
    'db': 'test',
    'host': 'localhost',
    'port': 27017,
    # 'username': 'webapp',
    # 'password': 'pwd123'
}


APP_PORT = 8080

