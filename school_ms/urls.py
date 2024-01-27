
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("Students.urls")),
    path("",include("staffs.urls")),
    path("academia/",include("academia.urls")),
    path("",include("lipa.urls")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)