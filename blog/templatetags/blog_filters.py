#!/usr/bin/env python
#coding=utf-8

from django.template import Library

register = Library()

@register.filter
def get_range(value):
    '''
    Filter: return a list containing range made from given value
    Usage(in template):
    
    <ul>
        {% for i in 3|get_range %}
        <li>{{ i }}. Do somting</li>
        {% endfor %}
    </ul>
    '''
    return range(value)