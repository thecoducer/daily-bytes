"""diary_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from diary_app import views
from diary_app.views import EntryListView

from django.conf.urls import include
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EntryListView.as_view(), name = 'home'),
    path('add/', views.add, name = 'add'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('about/', views.about),
    path('entry/<int:id>', views.readmore, name = 'readmore'),
    path('confirmdelete/<int:id>', views.confirmdelete),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('contact/', views.contact),
    path('no/', views.delete_no)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)