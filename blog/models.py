from django.db import models
from django.contrib.auth.models import User



class SimplePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    likers = models.ManyToManyField(User, related_name='likes')
    texte = models.TextField(null=True, blank=False,)
    image = models.ImageField(upload_to='posts/images', null=True, blank=True)
    video = models.FileField(upload_to='posts/videos', null=True, blank=True)

    def __str__(self):
        return f"publication de {self.user.username} le {self.time}"

    @property
    def likes(self):
        return self.likers.count()

    @likes.setter
    def likes(self, value):
        pass


class Menace(models.Model):
    destinataire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='menaces')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Menace sur "+self.destinataire.username
