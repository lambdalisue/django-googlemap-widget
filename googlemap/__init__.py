#!/usr/bin/env python
# vim: set fileencoding=utf8 :
"""Django Googlemap Library


Copyright:
    Copyright 2011 Alisue allright reserved.

License:
    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unliss required by applicable law or agreed to in writing, software
    distributed under the License is distrubuted on an "AS IS" BASICS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__author__  = 'Alisue <lambdalisue@hashnote.net>'
__version__ = '1.0.0'
__date__    = '2011/06/09'
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if not hasattr(settings, 'GOOGLEMAP_API_URL') and not hasattr(settings, 'GOOGLEMAP_API_SENSOR'):
    raise ImproperlyConfigured("You must define the GOOGLEMAP_API_SENSOR setting before using the field.")

# Google Map
settings.GOOGLEMAP_API_URL = getattr(settings, 'GOOGLEMAP_API_URL', r'http://maps.google.com/maps/api/js?sensor=%(sensor)s')
settings.GOOGLEMAP_SENSOR = getattr(settings, 'GOOGLEMAP_API_SENSOR')
# GoogleMapField
settings.GOOGLEMAP_SCRIPT_URL = getattr(settings, 'GOOGLEMAP_SCRIPT_URL', "javascript/django.googlemap.js")
settings.GOOGLEMAP_CLASS_NAME = getattr(settings, 'GOOGLEMAP_CLASS_NAME', 'django-googlemap-surface')

# Default values
from decimal import Decimal
settings.GOOGLEMAP_DEFAULT_LATITUDE = getattr(settings, 'GOOGLEMAP_DEFAULT_LATITUDE', Decimal("43.068625"))
settings.GOOGLEMAP_DEFAULT_LONGITUDE = getattr(settings, 'GOOGLEMAP_DEFAULT_LONGITUDE', Decimal("141.350801"))
settings.GOOGLEMAP_DEFAULT_ZOOM = getattr(settings, 'GOOGLEMAP_DEFAULT_ZOOM', 15)

