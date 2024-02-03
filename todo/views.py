from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
# Create your views here.
from todo.models import Task
from django.urls import reverse_lazy

class TaskListVies(ListView):
  model = Task
  tzemplate_name = 'todo/task_list.html'

class TaskDetailView(DetailView):
  model = Task
  template_name = "todo/task_detail.html"

class TaskCreateView(CreateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('task-list')
  