import os

import os.path
import collections

root_path = os.path.dirname(__file__)

def get_path(s):
    if isinstance(s, str):
        return os.path.join(root_path, s)
    elif isinstance(s, collections.Iterable):
        return os.path.join(root_path, os.sep.join(s))  

basepath=os.path.abspath(__file__)

path2=os.path.join(basepath)

#Templates
#TEMPLATE_DIRS=('/home/jacob/study/django/mysite/templates',)
path3=(os.path.join(os.path.dirname(__file__),'templates').replace('\\','/'),)
#path1=os.path
print os.path.abspath(__file__)
print root_path
print basepath
print (os.path.join(os.path.abspath(__file__)))
print path2
print path3
print get_path('static')
#print path1