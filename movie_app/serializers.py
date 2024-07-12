from rest_framework import serializers
from .models import Movie, Director, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'stars']

class MovieSerializer(serializers.ModelSerializer):
    review_set = serializers.SerializerMethodField()
    review_mean = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director', 'review_set', 'review_mean']

    def get_review_set(self, obj):
        reviews = obj.review_set.all()
        return ReviewSerializer(reviews, many=True).data

    def get_review_mean(self, obj):
        reviews = obj.review_set.all()
        if reviews:
            mean = sum(review.stars for review in reviews) / len(reviews)
            return round(mean, 1)
        return None
class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['name', 'movies_count']

    def get_movies_count(self, obj):
        return obj.movie_set.count()
