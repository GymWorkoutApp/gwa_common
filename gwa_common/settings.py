import os

from decouple import config

from gwa_framework.redis import RedisServer

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = config('DEBUG', default=False, cast=bool)
AUTO_RELOAD = config('AUTO_RELOAD', default=False, cast=bool)
PORT = config('PORT', default=8000, cast=int)
HOST = config('HOST', default='127.0.0.1')

# Settings tornado.web.Application.__init__
settings = {
    'debug': DEBUG,
    'autoreload': AUTO_RELOAD,
    'port': PORT,
    'host': HOST,
}


class LoggerSettings:
    LOGGER_NAME = f"lno-integrator-{config('PARTNER_NAME').lower()}-offers"
    LOGGER_APPLICATION = f"ecs-lno-integrator-{config('PARTNER_NAME').lower()}-offers"
    LOGGER_PRODUCT = f"serasa-{config('PARTNER_NAME').lower()}-offers"
    LOGGER_OUTPUT_FORMAT = 'JSON'


class Cache(RedisServer):
    REDIS_HOST = config('CACHE_HOST', default='localhost')
    REDIS_PORT = config('CACHE_PORT', default=6379)
