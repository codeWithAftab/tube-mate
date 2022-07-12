from django.contrib import admin
from django.urls import path , include
import downloader

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("downloader.urls"))

]
