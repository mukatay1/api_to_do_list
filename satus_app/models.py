from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class Info(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='+', blank=True, null=True,
                               verbose_name='Родитель')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def __repr__(self):
        return self.title


class Current(Info):
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)

    def subtitles(self):
        lst = []
        for i in Current.objects.filter(parent=self, is_completed=False):
            lst.append(i)
        return str(lst)

    def time_during(self):
        d = self.end - self.start
        return str(d)

    class Meta:
        verbose_name = 'Current'
        verbose_name_plural = 'Current'
        ordering = ['-start']


class List(Info):
    start = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'List'
        ordering = ['-start']


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photos/2022/04/25/user-default.png',
                              blank=True)

    def all_activity(self):
        return Current.objects.filter(author=self.user).count() + List.objects.filter(
            author=self.user).count()

    def number_completed(self):
        return Current.objects.filter(author=self.user, is_completed=True).count() + List.objects.filter(
            author=self.user, is_completed=True).count()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfile'
