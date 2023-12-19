from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from tele.views import *


urlpatterns = [
    path('', CreateArticle),
    path('<int:pk>', ShowArticle.as_view(), name='showArticle'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = pageNotFound

handler404 = pageNotFoundd

