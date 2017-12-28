from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from workatolist import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]

