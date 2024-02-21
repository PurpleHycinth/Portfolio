# Generated by Django 5.0 on 2023-12-07 05:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=255)),
                ("completed", models.BooleanField(default=False)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="task_images/"),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="TodoListItem",
        ),
    ]
