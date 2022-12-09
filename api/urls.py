from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from api.views import CessaoFundoViewSet
router = routers.DefaultRouter()
router.register(r'register', CessaoFundoViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls),name="api"),
]