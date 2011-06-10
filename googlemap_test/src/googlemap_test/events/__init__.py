from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth.management import create_superuser
from django.db.models import signals
#
# Automatically create test user at `syncdb`
#----------------------------------------------------------------------------------------------------
settings.AUTO_CREATE_USER = getattr(settings, 'AUTO_CREATE_USER', True)
if settings.DEBUG and settings.AUTO_CREATE_USER:
    # From http://stackoverflow.com/questions/1466827/ --
    #
    # Prevent interactive question about wanting a superuser created. (This code
    # has to go in this otherwise empty "models" module so that it gets processed by
    # the "syncdb" command during database creation.)
    #
    # Create our own test user automatically.
    def create_testuser(app, created_models, verbosity, **kwargs):
        USERNAME = 'admin'
        PASSWORD = 'admin'
        try:
            auth_models.User.objects.get(username=USERNAME)
        except auth_models.User.DoesNotExist:
            print '*' * 80
            print 'Creating test user -- login: %s, password: %s' % (USERNAME, PASSWORD)
            print '*' * 80
            assert auth_models.User.objects.create_superuser(USERNAME, 'x@x.com', PASSWORD)
        else:
            print 'Test user already exists. -- login: %s, password: %s' % (USERNAME, PASSWORD)
    signals.post_syncdb.disconnect(
        create_superuser,
        sender=auth_models,
        dispatch_uid='django.contrib.auth.management.create_superuser')
    signals.post_syncdb.connect(create_testuser,
        sender=auth_models, dispatch_uid='common.models.create_testuser')

#