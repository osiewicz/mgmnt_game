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

# DEBUG = False