import imp
from django.contrib import admin
from django.urls import path , include
from . import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("downloader.urls")) 

]
