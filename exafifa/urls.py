from django.urls import include, path
from rest_framework import routers

from exafifa.views import ExafifaViewSet

router = routers.DefaultRouter()
router.register("", ExafifaViewSet, basename="exafifa-viewset")

urlpatterns = [path("", include(router.urls))]
