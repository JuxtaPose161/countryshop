"""countryshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import mainshop.views
from countryshop import settings
from mainshop import urls as mainshop_urls
from users import urls as users_urls
from drf_part import urls as drf_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainshop.views.to_need_page),
    path('shop/', include(mainshop_urls)),
    path('auth/', include(users_urls, namespace='auth')),
    path('api/', include(drf_urls, namespace='api')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)