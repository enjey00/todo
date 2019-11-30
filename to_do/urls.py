from django.urls import path
from .views import *


urlpatterns = [
    path('user/', home, name='users_page'),
    path('add_todo/', add_todo, name=''),
    path('delete_todo/<int:todo_id>/', delete_todo),
]