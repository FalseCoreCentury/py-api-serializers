from rest_framework import serializers
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]
        read_only_fields = ("id", )


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]
        read_only_fields = ("id", )


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]
        read_only_fields = ("id", )


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True
    )
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
        read_only_fields = ("id", )

    def update(self, instance, validated_data):
        instance.show_time = validated_data.get(
            "show_time",
            instance.show_time
        )
        instance.movie = validated_data.get(
            "movie",
            instance.movie
        )
        instance.cinema_hall = validated_data.get(
            "cinema_hall",
            instance.cinema_hall
        )
        instance.save()
        return instance
