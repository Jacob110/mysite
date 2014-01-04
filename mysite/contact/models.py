#!/usr/bin/env python
#coding=utf-8

from django.db import models

class contact(models.Model):
	subject=models.CharField()
	email=models.EmailField()
	message=models.CharField()

	def __unicode__(self):
		return self.subject
    