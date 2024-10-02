from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tickets.urls')),  # Include the URLs from the tickets app
]


urlpatterns+=staticfiles_urlpatterns()