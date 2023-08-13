# Generated by Django 4.2.4 on 2023-08-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=150)),
                ('taskDescription', models.CharField(max_length=300)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
