from django.db import models
from django.contrib.auth.models import AbstractUser

from adoptar.settings.base import MEDIA_URL, STATIC_URL

# Create your models here.
class Province(models.Model):
    name = models.CharField(verbose_name="nombre", max_length=100)

    class Meta:
        verbose_name = "provincia"
        verbose_name_plural = "provincias"

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(verbose_name="nombre", max_length=200)
    province = models.ForeignKey(Province, verbose_name="provincia", on_delete=models.CASCADE)    

    class Meta:
        verbose_name = "ciudad"
        verbose_name_plural = "ciudades"

    def __str__(self):
        return self.name

class User(AbstractUser):
    avatar = models.ImageField(verbose_name="avatar", upload_to="users/%Y/%m/%d", null=True, blank=True)
    description = models.TextField(verbose_name="descripcion", blank=True, null=True, max_length=250)
    province = models.ForeignKey(Province, verbose_name="provincia", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    city = models.ForeignKey(City, verbose_name="ciudad", on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def get_avatar(self):
        if self.avatar:
            return '{}{}'.format(MEDIA_URL, self.avatar)
        return '{}{}'.format(STATIC_URL, 'images/empty.png')

class ReportReason(models.Model):
    title = models.CharField(verbose_name="titulo", max_length=100)

    class Meta:
        verbose_name = "razón"
        verbose_name_plural = "razones"

    def __str__(self):
        return self.title

class UserReport(models.Model):
    reason = models.ForeignKey(ReportReason, verbose_name="razon", on_delete=models.SET_NULL, null=True, blank=True)
    from_user = models.ForeignKey(User, verbose_name="denunciador", on_delete=models.SET_DEFAULT, default="Usuario", related_name="complaint_from_user")
    to_user = models.ForeignKey(User, verbose_name="denunciado", on_delete=models.DO_NOTHING, related_name="complaint_to_user")
    created_at = models.DateTimeField(verbose_name="creada", auto_now_add=True)
    comment = models.CharField(verbose_name="comentario", max_length=250, null=True, blank=True, default=None)

    class Meta:
        verbose_name = "denuncia"
        verbose_name_plural = "denuncias"

    def __str__(self):
        return "Denuncia #%s" % (self.pk)

class Qualification(models.Model):
    title = models.CharField(verbose_name="titulo", max_length=50)
    from_user = models.ForeignKey(User, verbose_name="calificador", on_delete=models.SET_NULL, related_name="qualification_from_user", null=True, blank=True)
    to_user = models.ForeignKey(User, verbose_name="calificado", on_delete=models.CASCADE, related_name="qualification_to_user")
    score = models.SmallIntegerField(verbose_name="puntución")
    created_at = models.DateTimeField(verbose_name="creada", auto_now_add=True)
    comment = models.CharField("comentario", max_length=200, null=True, default=None)
    

    class Meta:
        verbose_name = "calificación"
        verbose_name_plural = "calificaciones"

    def __str__(self):
        return "Puntuación %d - Usuario: %s" % (self.score, self.to_user.username)


