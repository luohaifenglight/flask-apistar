#! coding: utf-8

import logging
from utils.factory import app

from clannad.register import RegisterCenter

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] -'
                           '%(levelname)s: %(message)s',
                    level=logging.DEBUG)

RegisterCenter.register_blueprints(app)
logger = logging.getLogger("app")

logger.info(app.url_map)

server = app

if __name__ == '__main__':
    server.run(debug=True, port=app.config['APP_PORT'], host='0.0.0.0')
