from django.contrib import admin
from .models import Movie, CinemaHall, Seat, Session, Reservation, SessionSeat

admin.site.register(Movie)
admin.site.register(CinemaHall)
# admin.site.register(User)
admin.site.register(Seat)
admin.site.register(Session)
admin.site.register(Reservation)
admin.site.register(SessionSeat)