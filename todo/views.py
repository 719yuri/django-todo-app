from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from todo.models import Task

class TaskListView(ListView):
  model = Task
  template_name = 'todo/task_list.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/task_detail.html"