#!/usr/bin/env python
#coding=utf-8

from django.contrib import admin
from django.contrib.contenttypes import generic
from models import *

# Register your models here.

class CommentInline(generic.GenericStackedInline):
	model=Comment

class PostTagInline(admin.TabularInline):
	model=PostTag

class BlogPostAdmin(admin.ModelAdmin):
	list_display=('title','status','pub_date','slug')
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ('title', 'content')
	formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'class': 'mceEditor', 'rows': '50'})},
    }
	fieldsets = [
    	('文章编辑', {'fields': ('title', 'slug', 'content',)}),
    	
	]
	class Media:
	    js = ('/static/grappelli/js/tinymce/jscripts/tiny_mce/tiny_mce.js',
	    	'/static/grappelli/js/tinymce_setup/tinymce_setup.js',)
	        #"".join([mysite.settings.ADMIN_MEDIA_PREFIX,"tinymce_setup/tinymce_setup.js"]))
	inlines=(PostTagInline,)

class TagAdmin(admin.ModelAdmin):
	inlines=(PostTagInline,)
	prepopulated_fields={"slug":("name",)}

class CategoryAdmin(admin.ModelAdmin):
	list_display=('name','slug')

class CommentAdmin(admin.ModelAdmin):
	list_display=('msg_user','msg_email','msg_site'\
		,'msg_content','msg_avatar','msg_ip','msg_date','msg_obj',)
	list_per_page=10


admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Comment,CommentAdmin)