#! /usr/bin/env python
#coding=utf-8
from django import forms
from django.forms import ModelForm
from models import *

class ContactForm(ModelForm):
    class Meta:
    	fields="__all__"
    	model=contact
