STATIC_ROOT = "/home/hiro/zarzadzanie/static"
MEDIA_ROOT = "/home/hiro/zarzadzanie/media"
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'zarz.procesowe@gmail.com'
EMAIL_HOST_PASSWORD = 'Zarzadzanie1978'

DEBUG = True
PROJECT_COUNT = 9
MIN_RISK = 0.0
MAX_RISK = 1.0
MIN_COST = 15
MAX_COST = 25
MIN_PAYOFF = 10
MAX_PAYOFF = 30

WALLET_SIZE = 3
