# features/environment.py
import os
import django
from django.conf import settings


def before_all(context):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'Performance_tracking_app.settings'
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            INSTALLED_APPS=[
                'syncademic',
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'rest_framework',
            ],
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            }
        )
    django.setup()
