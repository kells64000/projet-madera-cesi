"""madera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework import routers

admin.autodiscover()

router = routers.DefaultRouter()

app_name = "madera"

urlpatterns = [

    # Url Dashboard Admin
    path('admin/', admin.site.urls),

    # Url API
    url(r'^api/', include(router.urls)),
    path('api/', include('addresses.api_urls')),
    path('api/', include('users.api_urls')),
    path('api/', include('quotes.api_urls')),
    path('api/', include('components.api_urls')),

    # Url API auth
    url(r'^auth/obtain_token/', obtain_jwt_token),
    url(r'^auth/refresh_token/', refresh_jwt_token),
    url(r'^auth/verify_token/', verify_jwt_token),

    # Url Template
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='Home'),

]

urlpatterns += staticfiles_urlpatterns()
