'''
@Author: your name
@Date: 2020-06-28 15:02:40
@LastEditTime: 2020-07-05 00:30:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python_project/bookmanager/book/admin.py
'''
from django.contrib import admin
from book.models import BookInfo
# Register your models here.
admin.site.register(BookInfo)
# admin.site.register(BookInfo)