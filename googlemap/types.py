#!/usr/bin/env python
# vim: set fileencoding=utf8 :
"""Django Googlemap Types


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
from decimal import Decimal

class Location(object):
    """Location which contain latitude, longitude, zoom"""
    @classmethod
    def parse(cls, value):
        """Parse formatted string to Location object
        
        Args:
            value - string formatted as `latitude, longitude, zoom`
        
        Return:
            Location instance
        """
        if isinstance(value, basestring):
            # TODO: Validation
            latitude, longitude, zoom = value.split(',')
            return cls(Decimal(latitude), Decimal(longitude), int(zoom))
        else:
            return value
    @classmethod
    def default(cls):
        return cls()
    
    def __init__(self, latitude=None, longitude=None, zoom=None):
        """Constructor
        
        Args:
            latitude - a latitude of location
            longitude - a longitude of location
            zoom - a zoom of map
        """
        self.latitude = latitude or settings.GOOGLEMAP_DEFAULT_LATITUDE
        self.longitude = longitude or settings.GOOGLEMAP_DEFAULT_LONGITUDE
        self.zoom = zoom or settings.GOOGLEMAP_DEFAULT_ZOOM
        
    def __str__(self):
        return self.__unicode__().encode('utf-8')
    
    def __unicode__(self):
        return u"%s, %s ,%d" % (
            self.latitude, 
            self.longitude,
            self.zoom,
        )