from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Genre, Actor, CinemaHall, Movie, MovieSession
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=["get"])
    def actors(self, request, pk=None):
        movie = self.get_object()
        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def genres(self, request, pk=None):
        movie = self.get_object()
        genres = movie.genres.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    @action(detail=True, methods=["get"])
    def movie_details(self, request, pk=None):
        session = self.get_object()
        movie = session.movie
        movie_serializer = MovieSerializer(movie)
        return Response(movie_serializer.data)

    @action(detail=True, methods=["get"])
    def cinema_hall_details(self, request, pk=None):
        session = self.get_object()
        cinema_hall = session.cinema_hall
        cinema_hall_serializer = CinemaHallSerializer(cinema_hall)
        return Response(cinema_hall_serializer.data)
