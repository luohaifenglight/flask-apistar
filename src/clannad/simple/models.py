#! coding: utf:8

from utils.collection import db
from utils.produceid import gen_uuid
from datetime import datetime


class SimpleCollection(db.Document):
    meta = {
        'collection': 'wx_app_conf',
        'ordering': ['-create_at'],
        'strict': False,
    }

    id = db.StringField(primary_key=True, default=gen_uuid)
    appid = db.StringField(required=True)
    secret = db.StringField(required=True)
    create_at = db.DateTimeField(default=datetime.now)
    template_id = db.StringField(required=True)

    def __str__(self):
        return str({
            'id': str(self.id),
            'appid': self.appid,
            'secret': self.secret,
            'template_id': self.template_id,
            'create_at': self.create_at.strftime("%Y-%m-%d %H:%M:%S")
        })
