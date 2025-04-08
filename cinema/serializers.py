from rest_framework import serializers
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]
        read_only_fields = "id"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]
        read_only_fields = "id"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]
        read_only_fields = "id"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]
        read_only_fields = "id"

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()

        if "genres" in validated_data:
            instance.genres.set(validated_data["genres"])

        if "actors" in validated_data:
            instance.actors.set(validated_data["actors"])

        return instance


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
        read_only_fields = "id"

    def update(self, instance, validated_data):
        instance.show_time = validated_data.get("show_time", instance.show_time)
        instance.movie = validated_data.get("movie", instance.movie)
        instance.cinema_hall = validated_data.get("cinema_hall", instance.cinema_hall)
        instance.save()
        return instance
