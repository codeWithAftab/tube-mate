from django.contrib import admin
from django.urls import path , include
from django.conf import settings #add this
from django.conf.urls.static import static #add this
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("downloader.urls")) 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
