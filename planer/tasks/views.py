from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm, TaskFormChange
from .models import *

menu = [
    {'name': 'Home', 'url_name': 'home'},
    {'name': 'Add Task', 'url_name': 'add'},
]


def index(request):
    tasks = Tasks.objects.all()
    context = {
        'title': 'Main page',
        'menu': menu,
        'tasks': tasks,
    }
    return render(request, 'tasks/index.html', context=context)


def add_tasks(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Wrong form!'

    form = TaskForm()
    context = {
        'title': 'Add Tasks',
        'menu': menu,
        'form': form,
        'error': error,
    }
    return render(request, 'tasks/add_tasks.html', context=context)


def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('home')


def change_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        form = TaskFormChange(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskFormChange(instance=task, initial={'title': task.title, 'task': task.task})

    context = {
        'form': form,
        'task': task,
        'task_id': task_id,
    }

    return render(request, 'tasks/change.html', context)
