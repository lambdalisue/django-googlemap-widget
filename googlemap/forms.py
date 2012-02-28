#!/usr/bin/env python
# vim: set fileencoding=utf8 :
"""Django Googlemap Field


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
from django.forms import MultiValueField, fields

from widgets import GoogleMapWidget, HiddenGoogleMapWidget
from types import Location

class GoogleMapField(MultiValueField):
    """GoogleMap form field"""
    widget          = GoogleMapWidget
    hidden_widget   = HiddenGoogleMapWidget
    
    def __init__(self, *args, **kwargs):
        field_list = (
            fields.DecimalField(max_value=90, min_value=-90, decimal_places=18, max_digits=25),
            fields.DecimalField(max_value=180, min_value=-180, decimal_places=18, max_digits=25),
            fields.IntegerField(),
        )
        if 'query_field_id' in kwargs:
            kwargs['widget'] = GoogleMapWidget(query_field_id=kwargs.pop('query_field_id'))

        super(GoogleMapField, self).__init__(field_list, *args, **kwargs)
        
    def compress(self, data_list):
        if not data_list:
            return ''
        return Location(data_list[0], data_list[1], data_list[2])
