
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('care.urls')),
    # path('', include('app3.urls')),
    path('', include('app4.urls')),


# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
] 
