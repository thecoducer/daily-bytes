from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=50, default='', verbose_name="")
    # text = RichTextField()
    text = RichTextUploadingField(verbose_name="")
    # verbose_name = "" is done to hide the labels
    date_posted = models.DateTimeField(auto_now_add = True)
    # auto_now_add gets the time when a entry is created

    # str is a text representation of each object in our model
    # objects corresponds to each row
    # id is the primary key in our table
    # it is an auto-incremented value
    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'
