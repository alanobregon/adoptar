# Generated by Django 3.0.10 on 2021-03-12 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='emisor'),
        ),
        migrations.AddField(
            model_name='chat',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='participantes'),
        ),
    ]