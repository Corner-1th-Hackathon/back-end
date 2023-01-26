from django.urls import include, path
from .views import PostViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    path('', include(router.urls)),
]