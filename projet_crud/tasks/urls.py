from django.urls import path
from . import views

urlpatterns=[
    path('',views.task_list, name='task_list'),
    path('create/',views.create_task, name='create_task'),
    path('update/<int:pk>/',views.task_update, name='task_update'),
    path('delete/<int:pk>/',views.task_delete, name='task_delete'),

]