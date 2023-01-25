"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from shop import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("list", views.list),
    path("list2", views.list2),
    path("list3", views.list3),
    path("list4", views.list4),
    path("list5", views.list5),
    path("list6", views.list6),
    path("list7", views.list7),
    path("list8", views.list8),
    path("list9", views.list9),
    path("list10", views.list10),
    path("list11", views.list11),
    path("list12", views.list12),
    path('', include('shop.urls')),
    path('insert', views.insert),
    path('detail/<int:post_code>', views.detail),
    path('accounts/', include('allauth.urls')),
    #path('tag/<str:slug>/', views.tag_page), #IP주소/blog/tag/slug/
    path('api/v1/shop/', include('shop.urls')),
    path('delete', views.delete),
]
