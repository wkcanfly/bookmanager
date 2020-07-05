'''
@Author: your name
@Date: 2020-06-28 15:02:40
@LastEditTime: 2020-06-30 15:43:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python_project/bookmanager/book/models.py
'''
from django.db import models

# Create your models here.
class BookInfo(models.Model):
    '''
    1.主键自动生成
    2.属性复制过来
    '''
    class Meta:
        # 改变数据库表名
        db_table='bookinfo'
        verbose_name= 'admin'
#    字段原来就是类属性啊
    name= models.CharField(max_length=10,unique=True)
    pub_date= models.DateField(null=True)
    readcount= models.IntegerField(default=0)
    commentcount= models.IntegerField(default=0)
    is_delete= models.BooleanField(default=False)
    # 一行数据对应一个对象所以使用__str__
    def __str__(self):
        return self.name
    

class PeopleInfo(models.Model):
    GENDER_CHOICES= (
        (0,'male'),
        (1,'female'),
    )
    name= models.CharField(max_length=10,verbose_name='名称')
    gender= models.SmallIntegerField(choices=GENDER_CHOICES,default=0,verbose_name='性别')
    description= models.CharField(max_length=200,null=True,verbose_name='描述')
    # 2.0之后外键必须加on_delete
    book= models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='书名')
    is_delete= models.BooleanField(default=False,verbose_name='逻辑删除')
    class Meta:
        db_table= 'peopleinfo'
        verbose_name= '书中人物信息'
    def __str__(self):
        return self.name  
