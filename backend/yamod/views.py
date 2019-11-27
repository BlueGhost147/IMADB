from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from yamod.models import Country, Movie
from yamod.serializers import CountryOptionSerializer, MovieListSerializer, MovieFormSerializer


@swagger_auto_schema(method='GET', responses={200: CountryOptionSerializer(many=True)})
@api_view(['GET'])
def country_option_list(request):
    countries = Country.objects.all()
    serializer = CountryOptionSerializer(countries, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: MovieListSerializer(many=True)})
@api_view(['GET'])
def movies_list(request):
    countries = Movie.objects.all()
    serializer = MovieListSerializer(countries, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=MovieFormSerializer, responses={200: MovieFormSerializer()})
@api_view(['POST'])
def movie_form_create(request):
    data = JSONParser().parse(request)
    serializer = MovieFormSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=MovieFormSerializer, responses={200: MovieFormSerializer()})
@api_view(['PUT'])
def movie_form_update(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = MovieFormSerializer(movie, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: MovieFormSerializer()})
@api_view(['GET'])
def movie_form_get(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie does not exist.'}, status=404)

    serializer = MovieFormSerializer(movie)
    return Response(serializer.data)


@api_view(['DELETE'])
def movie_delete(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response({'error': 'Movie does not exist.'}, status=404)
    movie.delete()
    return Response(status=204)
