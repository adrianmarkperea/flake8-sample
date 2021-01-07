import os

from flask import Flask
from flask_caching import Cache


app = Flask(__name__)

TEST_CACHE = 'simple'
PROD_CACHE = 'redis'

cache_type = TEST_CACHE if app.config['TESTING'] else PROD_CACHE
cache_config = {
    'CACHE_TYPE': cache_type,
    'CACHE_DEFAULT_TIMEOUT': 3600,
    # This is ignored if the cache_type isn't redis
    'CACHE_REDIS_URL': os.getenv('REDIS_URL'),
}
cache = Cache(app, config=cache_config)


import tmtest.routes
