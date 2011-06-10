#!/usr/bin/env python
# vim: set fileencoding=utf8 :
"""Django Googlemap templatetags


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
from django import template
from django.template.loader import render_to_string
from django.template import TemplateSyntaxError

register = template.Library()

class RenderGoogleMapHeadNode(template.Node):
    def render(self, context):
        context.push()
        html = render_to_string('googlemap/head.html', {}, context)
        context.pop()
        return html

@register.tag
def render_googlemap_head(parser, token):
    """Render javascript and css to be able the feature of editing tags
    
    Use this template tag in head block to be able the feature of editing tags.
    
    Syntax:
        {% render_googlemap_head %}
    """
    bits = token.split_contents()
    if len(bits) == 1:
        return RenderGoogleMapHeadNode()
    raise TemplateSyntaxError("%s tag never takes any arguments." % bits[0])