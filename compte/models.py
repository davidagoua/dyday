from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', default='avatars/default.jpg',null=True, blank=True)
    info = models.TextField(null=True, blank=True, help_text="Informations sur vous")
    address = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    abonnes = models.ManyToManyField(User, related_name='abonnements')
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args, **kwargs)


class NotificationBox(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='notebox')
    notifications = models.ManyToManyField('Notification', related_name='box', null=True, blank=True)

    def __str__(self):
        return f" NotificationBox ({self.user.username})"


class Notification(models.Model):
    text = models.TextField()
    link = models.URLField(null=True)
    lue = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link

    class Meta:
        ordering = ['-time']