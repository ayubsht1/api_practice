from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterUserViewSet
from authuser import views

router = DefaultRouter()
router.register(r'register', RegisterUserViewSet, basename='register')

urlpatterns = [
    path('api/', include(router.urls)),
    path("login/", views.LoginViewSet.as_view(), name= "login"),
]