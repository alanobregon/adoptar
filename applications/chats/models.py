from django.db import models

from applications.posts import models as posts
from applications.users import models as users

# Create your models here.
class Chat(models.Model):
    postulation = models.ForeignKey(posts.Postulation, verbose_name="postulación", on_delete=models.CASCADE)
    participants = models.ManyToManyField(users.User, verbose_name="participantes")

    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"

    def __str__(self):
        return "%d" % self.pk

class Message(models.Model):
    message = models.CharField(verbose_name="mensaje", max_length=2000)
    sender = models.ForeignKey(users.User, verbose_name="emisor", on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, verbose_name="chat", on_delete=models.CASCADE, related_name="messages")

    created_at = models.DateTimeField(verbose_name="enviado", auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return self.message