# Generated by Django 3.0.10 on 2021-03-12 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20210312_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='postulation',
        ),
    ]
