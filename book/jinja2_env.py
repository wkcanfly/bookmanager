'''
@Author: your name
@Date: 2020-07-05 00:05:56
@LastEditTime: 2020-07-05 10:45:04
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python_project/bookmanager/book/jinja2_env.py
'''
from jinja2 import Environment
#  'environment':'book.jinja2_env.environment',
def environment(**options):
    env = Environment(**options)
    return env