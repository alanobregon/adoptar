# Generated by Django 3.0.10 on 2021-03-09 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='PostStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='estado')),
            ],
            options={
                'verbose_name': 'estado de publicación',
                'verbose_name_plural': 'estado de publicaciones',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='titulo')),
                ('description', models.CharField(max_length=5000, verbose_name='descripción')),
                ('photo', models.ImageField(upload_to='posts/%Y/%m/%d', verbose_name='foto')),
                ('pet_name', models.CharField(max_length=50, verbose_name='nombre mascota')),
                ('pet_age', models.SmallIntegerField(verbose_name='edad aproximada')),
                ('cancel_comment', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='comentario de cancelacion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creada')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='actualizada')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creada por')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='posts.Category', verbose_name='categoria')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='posts.PostStatus', verbose_name='estado')),
            ],
            options={
                'verbose_name': 'publicación',
                'verbose_name_plural': 'publicaciones',
            },
        ),
    ]
