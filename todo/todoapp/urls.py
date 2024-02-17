from django.urls import path
from .views import ToDoDetail, ToDoUpdate


urlpatterns = [
    path('todos',ToDoDetail.as_view(),name="todo_list"), 
    path('todos/<int:pk>', ToDoUpdate.as_view(), name="todo_edit")
]
