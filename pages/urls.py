from django.urls import path

# Imports for serving media images on debug mode
from django.conf import settings
from django.conf.urls.static import static

from . import views as LocalViews

urlpatterns = [
    path('', LocalViews.HomePageView.as_view(), name='home'),
]

# url for serving media on debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)