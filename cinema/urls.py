from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register(r"genres", views.GenreViewSet)
router.register(r"actors", views.ActorViewSet)
router.register(r"cinema_halls", views.CinemaHallViewSet)
router.register(r"movies", views.MovieViewSet)
router.register(r"movie_sessions", views.MovieSessionViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
