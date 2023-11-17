"""
URL configuration for telegraph project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, re_path

from tele.views import *


urlpatterns = [
    path('', ArticleCreate.as_view()),
    # re_path(r'^(?P<year>[0-9]{2})-(?P<month>[0-9]{2})-(?P<day>[0-9]{4})$', ShowArticle.as_view(), name='showArticle2'),
    path('<int:pk>', ShowArticle.as_view(), name='showArticle'),
    path('home', home),
    path('admin/', admin.site.urls),
    # path('name', get_name),
    path('name', get_name_by_id.as_view()),
    path('add_okrig', add_okrig)
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
