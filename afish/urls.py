"""
URL configuration for afish project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from movie_app import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('users.urls')),

    # Режиссеры
    path('api/v1/directors/', views.director_list_api_views, name='director-list'),
    path('api/v1/directors/<int:id>/', views.director_detail_api_views, name='director-detail'),
    path('api/v1/directors/create/', views.director_create_api_view, name='director-create'),
    path('api/v1/directors/update/<int:id>/', views.director_update_api_view, name='director-update'),
    path('api/v1/directors/delete/<int:id>/', views.director_delete_api_view, name='director-delete'),

    # Фильмы
    path('api/v1/movies/', views.movie_list_api_views, name='movie-list'),
    path('api/v1/movies/<int:id>/', views.movie_detail_api_views, name='movie-detail'),
    path('api/v1/movies/create/', views.movie_create_api_view, name='movie-create'),
    path('api/v1/movies/update/<int:id>/', views.movie_update_api_view, name='movie-update'),
    path('api/v1/movies/delete/<int:id>/', views.movie_delete_api_view, name='movie-delete'),

    # Отзывы
    path('api/v1/reviews/', views.review_list_api_views, name='review-list'),
    path('api/v1/reviews/<int:id>/', views.review_detail_api_views, name='review-detail'),
    path('api/v1/reviews/create/', views.review_create_api_view, name='review-create'),
    path('api/v1/reviews/update/<int:id>/', views.review_update_api_view, name='review-update'),
    path('api/v1/reviews/delete/<int:id>/', views.review_delete_api_view, name='review-delete'),

    # Список фильмов с отзывами
    path('api/v1/movies/reviews/', views.movie_reviews_list, name='movie-review-list'),

]
