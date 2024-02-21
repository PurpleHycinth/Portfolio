from django.db import models

class TodoListItem(models.Model):
    content = models.TextField()
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True)

    def __str__(self):
        return self.content


