#!/usr/bin/env python
#coding=utf-8

from datetime import datetime
from django.db import models
from django.db.models import permalink
from django import forms
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

import re
#from django.contrib import admin
import mysite

#Get article abstract
_pagebreak="<p><!-- pagebreak --></p>"
get_abstract=lambda s: s.split(_pagebreak)[0]
# Create your models here.
# Category Model
class Category(models.Model):
	name=models.CharField(max_length=50,unique=True,verbose_name='分类名')
	slug=models.SlugField()
	
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name="分类"
		verbose_name_plural="分类"

	@permalink
	def get_absolute_url(self):
		return('blog_category',None,{'slug':self.slug})

# Tag Model
class Tag(models.Model):
	name=models.CharField(max_length=50,unique=True,verbose_name='标签名')
	slug=models.SlugField()

	class Meta:
		verbose_name='标签'
		verbose_name_plural='标签'
		ordering=['?']

	def __unicode__(self):
		return self.name

# Post Model
class BlogPost(models.Model):
	STATUS_CHOICE=(
		(1,'编辑'),
		(2,'完成'),
		(3,'丢弃'),
	)
	title=models.CharField(max_length=100,verbose_name='标题')
	slug=models.SlugField(max_length=100)
	content=models.TextField(verbose_name='content')
	status=models.IntegerField(choices=STATUS_CHOICE,default=1,verbose_name='文章状态')
	pub_date=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
	up_date=models.DateTimeField(default=datetime.now,verbose_name='更新时间')
	category=models.ForeignKey(Category,blank=True,null=True)
	tags=models.ManyToManyField(Tag,blank=True,null=True,through='PostTag',verbose_name='标签')
	clicks=models.IntegerField(default=0,editable=False,verbose_name='点击次数')
	# Comment
	comments=generic.GenericRelation('Comment')

	def __unicode__(self):
		return self.title
	@permalink
	def get_absolute_url(self):
		return('blog_article',None,{'slug':self.slug})
	def __getattr__(self,name):
		if(name=="abstract"):
			return get_abstract(self.content)
		return super(BlogPost, self).__getattr__(name)
	
	#点击次数
	def click_count(self):
		self.clicks+=1
		super(BlogPost,self).save()

	class Meta:
		verbose_name='文章'
		verbose_name_plural='文章'
		ordering=['pub_date']

# PostTag Model
class PostTag(models.Model):
	article=models.ForeignKey(BlogPost)
	tag=models.ForeignKey(Tag)

	class Meta:
		verbose_name="文章标签"
		verbose_name_plural="文章标签"
	def __unicode__(self):
		return unicode(self.tag)
# Comment manager
from mptt.managers import TreeManager
from django.db.models import Q
class CommentToPostManager(TreeManager):
	def get_query_set(self):
		return super(CommentToPostManager,self).get_query_set()\
			.filter(Q(content_type__model="blogPost"))

# Comment model
from mptt.models import MPTTModel,TreeForeignKey
class Comment(MPTTModel):
	
	msg_user=models.CharField(max_length=60,verbose_name='用户名')
	msg_email=models.EmailField(verbose_name='邮箱地址')
	msg_content=models.TextField(verbose_name='内容')
	msg_site=models.URLField(max_length=255,blank=True,verbose_name='个人网站')
	msg_avatar=models.URLField(blank=True,null=True,verbose_name='头像')
	msg_date=models.DateTimeField(editable=False,default=datetime.now,verbose_name='评论日期')
	msg_ip=models.IPAddressField(null=True,blank=True,verbose_name='IP地址')
	# replay
	msg_reply=models.ForeignKey('self',null=True,blank=True,related_name='children')

	content_type=models.ForeignKey(ContentType)
	object_id=models.PositiveIntegerField()
	msg_obj=generic.GenericForeignKey('content_type','object_id')

	# Managers
	objects=TreeManager()
	to_post_objects=CommentToPostManager()

	class Meta:
		ordering=['-msg_date']
		verbose_name='评论'
		verbose_name_plural='评论'

	class MPTTMeta:
		"""docstring for MPTTMeta"""
		parent_attr='msg_reply'
		
	def __unicode__(self):
		return self.msg_content