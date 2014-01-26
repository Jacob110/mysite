#! /usr/bin/env python
#coding=utf-8

from django import template

register=template.Library()

@register.simple_tag
def nav_item_selected(request,pattern):	
	#print pattern
	#print request.path
	import re
	if re.search(pattern,request.path):
	#Current nav item CSS style
		return "selected"
	else:
		return ""
	