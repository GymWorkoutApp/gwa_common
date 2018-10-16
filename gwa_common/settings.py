import os

from decouple import config
from gwa_framework.redis import RedisServer

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = config('DEBUG', default=False, cast=bool)
AUTO_RELOAD = config('AUTO_RELOAD', default=False, cast=bool)
PORT = config('PORT', default=8000, cast=int)
HOST = config('HOST', default='127.0.0.1')

GWA_ENVIRONMENT = config('GWA_ENVIRONMENT')


class GWAAppConfig:

    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DatabaseConfig.DB_USER}:{DatabaseConfig.DB_PASSWORD}' \
                                                f'@{DatabaseConfig.DB_HOST}/{DatabaseConfig.DB_NAME}'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class DatabaseConfig:
    DB_HOST = config('DB_HOST', default='postgresql://127.0.0.1:5432')
    DB_USER = config('DB_USER', default='gwa_common')
    DB_PASSWORD = config('DB_PASSWORD', default='D1685E7932B7B71F138CECE1C0300414')
    DB_NAME = config('DB_NAME', default='gwa_common_db')


class LoggerSettings:
    LOGGER_NAME = f"gwa-common"
    LOGGER_APPLICATION = f"gwa-common.server"
    LOGGER_PRODUCT = f"gwa"
    LOGGER_OUTPUT_FORMAT = 'JSON'


class Cache(RedisServer):
    REDIS_HOST = config('CACHE_HOST', default='localhost')
    REDIS_PORT = config('CACHE_PORT', default=6379)
