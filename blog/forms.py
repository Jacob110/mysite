#! /usr/bin/env python
#coding=utf-8

from django import forms
from django.forms import ModelForm
from django.contrib.contenttypes.models import ContentType
from models import Comment

# Class CommentForm
class CommentForm(ModelForm):
	msg_user=forms.CharField(
			widget=forms.TextInput(attrs={
						'id':'name',
						'placeholder':'昵称',
						'tabindex':'1',
						'onfocus':"inputFocusOrBlur(this,0,'昵称')",
						'onblur':"inputFocusOrBlur(this,1,'昵称')"
					}),max_length=50)
	msg_email=forms.EmailField(
			widget=forms.TextInput(attrs={
					'id':'email',
					'placeholder':'邮箱',
					'tabindex':'2',
					'onfocus':"inputFocusOrBlur(this,0,'邮箱')",
					'onblur':"inputFocusOrBlur(this,1,'邮箱')"
				}),max_length=75)
	msg_site=forms.URLField(
			widget=forms.TextInput(attrs={
					'id':'website',
					'placeholder':'网站',
					'tabindex':'3',
					'onfocus':"inputFocusOrBlur(this,0,'网站')",
					'onblur':"inputFocusOrBlur(this,1,'网站')"
				}),required=False,max_length=200)
	msg_content=forms.CharField(
			widget=forms.Textarea(attrs={
					'id':'message',
					'rows':'3',
					'cols':'50',
					'tabindex':'4'
				}))

	# Hidden Input
	msg_avatar = forms.URLField(widget=forms.HiddenInput, required=False)
	msg_reply=forms.ModelChoiceField(Comment.objects.all(),widget=forms.HiddenInput(), required=False)
	content_type=forms.ModelChoiceField(ContentType.objects.all(), widget=forms.HiddenInput())
	object_id=forms.IntegerField(widget=forms.HiddenInput())

	class Meta:
		fields="__all__"
		model=Comment
		#fields=['msg_user','msg_email','msg_content','msg_content','msg_site','msg_avatar','msg_reply','content_type','object_id']
