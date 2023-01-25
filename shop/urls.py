from django.urls import include, path
from .views import PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls'))
]