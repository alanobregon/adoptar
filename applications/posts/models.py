from django.db import models

from applications.users.models import User
from adoptar.settings.base import MEDIA_URL, STATIC_URL

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="nombre", max_length=50)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.name

class PostStatus(models.Model):
    status = models.CharField(verbose_name="estado", max_length=50)

    class Meta:
        verbose_name = "estado de publicación"
        verbose_name_plural = "estado de publicaciones"

    def __str__(self):
        return self.status

class Post(models.Model):
    title = models.CharField(verbose_name="titulo", max_length=100)
    description = models.CharField(verbose_name="descripción", max_length=5000)
    photo = models.ImageField(verbose_name="foto", upload_to="posts/%Y/%m/%d")
    status = models.ForeignKey(PostStatus, verbose_name="estado", on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, verbose_name="categoria", on_delete=models.DO_NOTHING)
    pet_name = models.CharField(verbose_name="nombre mascota", max_length=50)
    pet_age = models.SmallIntegerField(verbose_name="edad aproximada")
    author = models.ForeignKey(User, verbose_name="creada por", on_delete=models.CASCADE)
    cancel_comment = models.CharField(verbose_name="comentario de cancelacion", max_length=500, null=True, default=None, blank=True)

    created_at = models.DateTimeField(verbose_name="creada", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="actualizada", auto_now=True)

    class Meta:
        verbose_name = "publicación"
        verbose_name_plural = "publicaciones"

    def __str__(self):
        return self.title

    def get_photo(self):
        if self.photo:
            return '{}{}'.format(MEDIA_URL, self.photo)
        return '{}{}'.format(STATIC_URL, 'images/no_photo.png')