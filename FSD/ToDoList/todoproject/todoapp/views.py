# todoapp/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import TodoListItem
from .forms import TaskForm

def todoappView(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todoapp/')

    all_todo_items = TodoListItem.objects.all()
    completed_todo_items = TodoListItem.objects.filter(completed=True)

    form = TaskForm()
    return render(request, 'index.html', {
        'all_items': all_todo_items,
        'completed_items': completed_todo_items,
        'form': form
    })

def deleteTodoView(request, todo_id):
    todo_item = TodoListItem.objects.get(id=todo_id)
    todo_item.delete()
    return HttpResponseRedirect('/todoapp/')
