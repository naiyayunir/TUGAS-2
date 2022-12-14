from django.urls import path
from todolist.views import create_task, get_todolist_json, register_pengguna, show_todolist
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import *


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register_pengguna, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task', create_task, name='create_task'),
    path('json/',get_todolist_json,name="get_todolist_json"),
    path('add/', add_todolist, name='add_todolist'),
]
