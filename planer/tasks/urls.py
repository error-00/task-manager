from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-tasks', views.add_tasks, name='add'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('change_task/<int:task_id>', views.change_task, name='change_task'),
]
