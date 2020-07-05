'''
@Author: your name
@Date: 2020-06-29 14:24:23
@LastEditTime: 2020-07-02 14:28:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python_project/bookmanager/book/urls.py
'''
from django.urls import path,re_path
from book.views import LoginView
app_name= 'book'
urlpatterns = [
    # re_path(r'^(?P<category_id>\d+)/(?P<book_id>\d+)/$', LoginView.as_views(),name='index')
    re_path(r'^', LoginView.as_view(),name='LoginView')
]