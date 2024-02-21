# todo_project/todo_app/forms.py
from django import forms
from .models import TodoListItem

class TaskForm(forms.ModelForm):
    class Meta:
        model = TodoListItem
        fields = ['content', 'completed', 'image']
