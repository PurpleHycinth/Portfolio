# Generated by Django 5.0 on 2023-12-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todoapp", "0002_task_delete_todolistitem"),
    ]

    operations = [
        migrations.CreateModel(
            name="TodoListItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("completed", models.BooleanField(default=False)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="todo_images/"),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Task",
        ),
    ]
