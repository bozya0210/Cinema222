from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),  # Маршрут для страницы "Расписание"
    path('profile/', views.profile, name='profile'),  # Маршрут для страницы "Личный кабинет"
    path('theaters/', views.theaters, name='theaters'),  # Маршрут для страницы "Наши кинотеатры"
    path('upcoming/', views.upcoming, name='upcoming'),  # Маршрут для страницы "Скоро в кино"
    path('promotions/', views.promotions, name='promotions'),  # Маршрут для страницы "Акции"
    path('news/', views.news, name='news'),  # Маршрут для страницы "Новости"
]