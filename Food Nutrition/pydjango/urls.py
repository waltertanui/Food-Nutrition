"""
URL configuration for pydjango project.

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




from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
# {{ edit_1 }}
from django.views.generic.base import RedirectView
from myApp import views

urlpatterns = [
    # {{ edit_2 }}
    # Redirect the root URL to the myApp index page
    path('', RedirectView.as_view(url='/myApp/index/', permanent=False), name='index_redirect'),
    path('myApp/', include('myApp.urls')),  # 保留这种引入方式，方便以myApp为前缀访问相关路径
    path('weekly-recipes/', views.weekly_recipes, name='weekly_recipes'),
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

