from django.conf.urls import patterns, include, url

from django.contrib import admin
import books.views
import mytweepy.views
import contact.views
import blog.views
admin.autodiscover()

from mysite.view import current_datetime,hours_ahead
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
    url(r'^admin/', include(admin.site.urls)),
    (r'^time/$',current_datetime),
    (r'^time/plus/(\d{1,2})/$',hours_ahead),
    (r'^search_form/$',books.views.search_form),
    (r'^search/$',books.views.search),

    url(r'^contact/$',TemplateView.as_view(template_name='contact_form.html'),name="contactform"),
    url(r'^contact/add/$',contact.views.contact,name="contact"),
    #(r'^search_results/$',views.search_results),
    url(r'^index$',TemplateView.as_view(template_name='index.html'),name="index"),
    url(r'^profile$',TemplateView.as_view(template_name='profile.html'),name="profile"),
    #Twitter API page
    url(r'^mytweepy',mytweepy.views.get_tweets,name='twitter'),
    #Articles page
    url(r'^blog',blog.views.show_articles,name='blog'),
    url(r'^grappelli/',include('grappelli.urls')),

    url(r'^comment/add/$',blog.views.comment,name='post_comment'),
    #Article page
    url(r'^article/(?P<slug>[-\w]+)/$',blog.views.article,name='blog_article'),
)
