from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=30, default='')
    text = models.TextField()
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
