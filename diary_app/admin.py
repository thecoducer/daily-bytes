from django.contrib import admin
from diary_app.models import Entry, UserData

# Register your models here.

admin.site.register(Entry)
admin.site.register(UserData)