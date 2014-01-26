#! usr/bin/env python
# coding=utf-8

from django.conf.urls import patterns,url
from views import *

urlpatterns=patterns(
	'',
	# Index page (articles default)
	url(r'^$',show_articles,name='blog'),
	# Article page (single article)
    url(r'^article/(?P<slug>[-\w]+)/$',article,name='blog_article'),
    # Category post
    url(r'^category/(?P<slug>\w+)/$',category,name='blog_category'),
    # Tag post
    url(r'^tag/(?P<slug>\w+)/$','tag',name='blog_tag'),
    # Archive
    url(r'archive/$',archive,name='blog_archive'),
    # Archive post
    url(r'archive/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',archive_date_slug_post,name='blog_archive_detail'),
)