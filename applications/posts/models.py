from django.db import models

from applications.chats.models import Chat
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
    author = models.ForeignKey(User, verbose_name="creada por", on_delete=models.CASCADE, related_name="my_posts")
    cancel_comment = models.CharField(verbose_name="comentario de cancelacion", max_length=500, null=True, default=None, blank=True)

    postulations = models.ManyToManyField(User, verbose_name="postulaciones", through="Postulation")

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

    def get_status(self):
        return self.status.status

class PostulationStatus(models.Model):
    status = models.CharField(verbose_name="estado", max_length=50)

    class Meta:
        verbose_name = "estado de postulación"
        verbose_name_plural = "estado de postulaciones"

    def __str__(self):
        return self.status

class Postulation(models.Model):
    candidate = models.ForeignKey(User, verbose_name="candidato", on_delete=models.CASCADE, related_name="my_postulations")
    post = models.ForeignKey(Post, verbose_name="publicacion", on_delete=models.CASCADE)
    status = models.ForeignKey(PostulationStatus, verbose_name="estado", on_delete=models.DO_NOTHING)

    chat = models.OneToOneField(Chat, verbose_name="chat", on_delete=models.SET_NULL, null=True, default=None, auto_created=True)

    comment = models.CharField(verbose_name="comentario", max_length=1000, default=None, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="creada", auto_now_add=True)
    class Meta:
        verbose_name = "postulaciones"
        verbose_name_plural = "postulaciones"

    def __str__(self):
        return "%d" % self.pk
