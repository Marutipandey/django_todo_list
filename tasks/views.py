from django.shortcuts import render, redirect
from .models import Task

from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    completed_tasks = tasks.filter(completed=True)
    not_completed_tasks = tasks.filter(completed=False)
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'not_completed_tasks': not_completed_tasks,
        'completed_count': completed_tasks.count(),
        'not_completed_count': not_completed_tasks.count()
    }
    return render(request, 'tasks/task_list.html', context)


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        completed = bool(int(request.POST['completed']))
        Task.objects.create(title=title, completed=completed)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

def mark_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def mark_not_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = False
    task.save()
    return redirect('task_list')
