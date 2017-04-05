from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_jMrqEWUObXQYcsowwHCjDJ2E')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_lBEnGIqQGKUW4nXQh05GkxLE')


SITE_URL = 'https://property-mogul.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://property-mogul.herokuapp.com/a-really-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'property.mogul@philip.com'
PAYPAL_TEST = True