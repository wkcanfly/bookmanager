'''
@Author: your name
@Date: 2020-06-28 15:02:40
@LastEditTime: 2020-07-05 12:33:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python_project/bookmanager/book/views.py
'''
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# from django.db.models import F
from book.models import BookInfo
# Create your views here.
from django.views import View
class LoginView(View):
    def get(self,request):
        # request.session.clear()
        # del request.session['sessionid']
        # request.session.flush()
        if request.COOKIES.get('sessionid'):
            print(request.COOKIES.get('sessionid'))
            # HttpResponse.delete_cookie('sessionid')
        # print(request.COOKIES.get('sessionid'))
            # request.session.clear()
        # return HttpResponse('登录界面')
        request.session['name']= 'itcast'
        books= BookInfo.objects.all()
        context= {
             'books': books,

        }
        return render(request,'book/index.htm',context)
        # return HttpResponse('abcd');

    def post(self,request):
        return HttpResponse('登录验证')    

# def index(resquest,category_id,book_id):
#     print(category_id,book_id)
#     books= BookInfo.objects.all()
#     context = {
#         'books': books
#     }
#     # print(__file__)
#     # print(os.path)

#     return render(resquest, 'book/index.htm', context)
#     # return HttpResponse('index')

      