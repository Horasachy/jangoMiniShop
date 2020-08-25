from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count()

user = 'www'
bind = '127.0.0.1:8001'
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()
reload = True
name = 'jangoMiniShop'

env = {
    'DJANGO_SETTINGS_MODULE': 'jangoMiniShop.settings'
}
