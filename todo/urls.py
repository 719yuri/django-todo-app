
from django.urls import path

from todo.views import TaskListVies, TaskDetailView, TaskCreateView


urlpatterns = [
    path('', TaskListVies.as_view(), name='task-list'),
    path('task/new/', TaskCreateView.as_view(), name='task-new'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail')
]

