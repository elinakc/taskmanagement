# Generated by Django 5.1.1 on 2024-10-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.TextField(max_length=255, null=True),
        ),
    ]