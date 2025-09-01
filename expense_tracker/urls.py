from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import UserViewSet, user_login, CategoryViewSet


router = DefaultRouter()
router.register('users',UserViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('login/', user_login),
]
