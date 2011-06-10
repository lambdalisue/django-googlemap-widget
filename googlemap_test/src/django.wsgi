# Append to the PYTHONPATH
import os, sys
ROOT = os.path.join(os.path.dirname(__file__), '../')

path_list = [
    os.path.join(ROOT, 'src'),
    os.path.join(ROOT, '../../'),
]
for path in path_list:
    if path not in sys.path:
        sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'universaltag_test.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
