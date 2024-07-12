from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from django.db.models import Prefetch
from rest_framework import status

@api_view(['GET'])
def director_list_api_views(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def director_detail_api_views(request, id):
    try:
        director = Director.objects.get(id=id)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def director_create_api_view(request):
    serializer = DirectorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def director_update_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DirectorSerializer(director, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def director_delete_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    director.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def movie_list_api_views(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail_api_views(request, id):
    try:
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def movie_create_api_view(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def movie_update_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializer(movie, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def movie_delete_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review_detail_api_views(request, id):
    try:
        review = Review.objects.get(id=id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def review_list_api_views(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def review_create_api_view(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def review_update_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ReviewSerializer(review, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def review_delete_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def movie_reviews_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def directors_list(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)
