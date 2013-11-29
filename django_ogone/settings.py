'''
The following settings should be defined in your global settings

SHA_PRE and SHA_POST_SECRET have to be set in the ogone admin
Can be any random value. Its just something secret both us and ogone need to know.

Note that the default hash method is set to sha512
Change this in your ogone admin interface

'''

try:
    from django.conf import settings
except ImportError:
    # We do not need Django to used this package
    settings = {}

#These four you probably want to change
OGONE_PSPID = getattr(settings, 'OGONE_PSPID', None)
OGONE_SHA_PRE_SECRET = getattr(settings, 'OGONE_SHA_PRE_SECRET', None)
OGONE_SHA_POST_SECRET = getattr(settings, 'OGONE_SHA_POST_SECRET', None)
OGONE_CURRENCY = getattr(settings, 'OGONE_CURRENCY', 'EUR')

#only touch these if you know whats happening :P
OGONE_HASH_METHOD = getattr(settings, 'OGONE_HASH_METHOD', 'sha512')
#for other hashmethods see http://docs.python.org/library/hashlib.html
#ogone default is sha1
OGONE_PRODUCTION = not getattr(settings, 'DEBUG', True)

# Standard URLs. We might want to override these in the future for some
# reason.
OGONE_TEST_URL = getattr(settings, "OGONE_TEST_URL",
    "https://secure.ogone.com/ncol/test/orderstandard.asp")
OGONE_PROD_URL = getattr(settings, "OGONE_PROD_URL",
    "https://secure.ogone.com/ncol/prod/orderstandard.asp")

# DirectLink
OGONE_API_USRID = getattr(settings, 'OGONE_API_USRID', None)
OGONE_API_PSWD = getattr(settings, 'OGONE_API_PSWD', None)

OGONE_DIRECT_LINK_TEST_URL = getattr(settings, "OGONE_DIRECT_LINK_TEST_URL",
    "https://secure.ogone.com/ncol/test/orderdirect.asp")
OGONE_DIRECT_LINK_PROD_URL = getattr(settings, "OGONE_DIRECT_LINK_PROD_URL",
    "https://secure.ogone.com/ncol/prod/orderdirect.asp")
