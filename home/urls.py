from django.contrib import admin
from django.urls import path,include
from home import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('todos/',views.todos.as_view(),name="todos"), 
    path('todo/<int:pk>',views.todo.as_view(),name="todo"), 
]
