#!/usr/bin/env python
#coding=utf-8

import urllib2,hashlib
import re
from django.utils.html import escape
from django.db.models import Q,Count,Max,Min

from django.shortcuts import render_to_response,get_object_or_404
from django.template import loader,Context
from django.http import HttpResponse,Http404
from django.contrib.contenttypes.models import ContentType
from django.core.context_processors import csrf
from forms import CommentForm
#from blog.models import BlogPost
from models import *

# Create your views here.

# blog post single
def article(request,slug):
	# To do
	#try:
		#post=get_object_or_404(BlogPost,slug)
	post=BlogPost.objects.get(slug=slug)
		#print slug
	#except post.DoesNotExist:
		#pass
		#print post.title
	#print post
	nodes=Comment.to_post_objects.filter(object_id=post.id)
	#Comment form
	content_type=ContentType.objects.get(model='BlogPost')
	comment_instance=Comment(content_type=content_type,object_id=post.id)
	form=CommentForm(instance=comment_instance)
	data={
		'post':post,
		'form':form,
		'nodes':list(nodes),
		'slug':slug
	}
	data.update(csrf(request))

	return render_to_response('article.html',data)

# blog post list
def show_articles(request):
	posts=BlogPost.objects.all()
	#nodes=Comment.to_post_objects.filter(object_id=posts.id)
	# for post in posts:
	# 	print post.slug
	# 	print post.get_absolute_url
	form=CommentForm()
	data={
		'posts':posts,
		'f':form,
	}
	data.update(csrf(request)) # add this resolve 'CSRF verification failed. Request aborted.'
	
	return render_to_response('articleList.html',data)

# Comment views
process_comment=lambda content:escape(content).replace('\n','<br />')

def comment(request):
	response=HttpResponse()

	# rqData={
	# 	'msg_user':'Jacob',
	# 	'msg_email':'yjj.jacob@gmail.com',
	# 	'msg_site':'',
	# 	'msg_content':'comment',
	# 	'msg_avatar':'',
	# 	'msg_reply':'',
	# 	'content_type':22,
	# 	'object_id':3,
	# }	
	#f=CommentForm(rqData)	
	comment_instance=Comment()
	f=CommentForm(request.POST)
	#print f.errors	
	#print f.is_valid()	
	if f.is_valid():
				
		comment=f.save()
		response.write(f.is_valid())
		# comment.msg_content=process_comment(comment.msg_content)

		# access_gravatar=False
		# if not comment.msg_avatar or len(comment.msg_avatar.strip())==0:
		# 	email_hash=hashlib.md5(comment.email_address.strip()).hexdigest()
		# 	try:
		# 		avatar_url='http://www.gravatar.com/avatar/%s?s=40&d=404' % email_hash
		# 		urllib2.urlopen(avatar_url)
		# 		comment.msg_avatar=avatar_url
		# 		access_gravatar=True
		# 	except urllib2.URLError:
		# 		comment.avatar=''
		# comment.save()
		print comment.id
		response.write(str(comment.id))
	else:
		#pass		
		response.write("0")
	return response



