from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_id>/booking/<int:session_id>/', views.show_seats_selection, name='booking_page'),
    # Страница выбора мест
    path('process_seats_selection/', views.process_seats_selection, name='process_seats_selection'),
    # Обработка выбранных мест
]
