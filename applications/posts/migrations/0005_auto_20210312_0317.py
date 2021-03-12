# Generated by Django 3.0.10 on 2021-03-12 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_remove_chat_postulation'),
        ('posts', '0004_postulation_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulation',
            name='chat',
            field=models.OneToOneField(auto_created=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='chats.Chat', verbose_name='chat'),
        ),
    ]