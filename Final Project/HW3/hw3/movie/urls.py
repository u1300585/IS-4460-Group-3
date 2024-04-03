from django.urls import path
from . import views
from .views import MovieListCreateView, MovieDetailView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('list/', views.MovieList.as_view(), name='movie-list'),
    path('detail/<int:pk>/', views.MovieDetailView.as_view(), name='movie-details'),
    path('update/<int:pk>/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('delete/<int:pk>/', views.MovieDeleteView.as_view(), name='movie-delete'),
    path('movie-add/',views.MovieAdd.as_view(), name='movie-add'),
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(),name='movie-details'),
    path('customer-list/', views.customer_list, name='customer-list'),
]
