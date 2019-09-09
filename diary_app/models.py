from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # User is an auth model
    title = models.CharField(max_length=100, default='', verbose_name="")
    # text = RichTextField()
    text = RichTextUploadingField(verbose_name="")
    # verbose_name = "" is done to hide the labels
    date_posted = models.DateTimeField(auto_now_add = True)
    # auto_now_add gets the time when a entry is created
    trash = models.BooleanField(default=False)
    # str is a text representation of each object in our model
    # objects corresponds to each row
    # id is the primary key in our table
    # it is an auto-incremented value
    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = 'entries'


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return '{}'.format(self.user)