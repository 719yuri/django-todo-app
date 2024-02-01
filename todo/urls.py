
from django.urls import path

from todo.views import TaskListVies, TaskDetailView


urlpatterns = [
    path('', TaskListVies.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail')
]

