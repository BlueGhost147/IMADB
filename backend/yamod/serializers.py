from rest_framework import serializers
from .models import Country, Movie


class CountryOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class MovieListSerializer(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'country_name']

    def get_country_name(self, obj):
        return obj.country.name if obj.country else ''


class MovieFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'