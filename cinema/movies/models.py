from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     role_choices = [
#         ('admin', 'Администратор'),
#         ('user', 'Пользователь')
#     ]
#     role = models.CharField(max_length=20, choices=role_choices)
#
#     def __str__(self):
#         return self.name
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.title


class CinemaHall(models.Model):
    hall_choices = [
        ('2D_1', 'Зал 1 - 2D'),
        ('2D_2', 'Зал 2 - 2D'),
        ('2D_3', 'Зал 3 - 2D'),
        ('3D_4', 'Зал 4 - 3D'),
        ('VIP_5', 'Зал 5 - VIP'),
        ('VIP_3D_6', 'Зал 6 - VIP 3D'),
    ]
    hall_name = models.CharField(max_length=10, choices=hall_choices)

    def __str__(self):
        return self.get_hall_name_display()

class Seat(models.Model):
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    row_number = models.IntegerField()
    seat_number = models.IntegerField()
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Row {self.row_number}, Seat {self.seat_number} in {self.cinema_hall.get_hall_name_display()}"

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} at {self.start_time}"

class Reservation(models.Model):
    movie_session = models.ForeignKey(Session, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_email = models.EmailField()
    reservation_time = models.DateTimeField()

    def __str__(self):
        movie_title = self.movie.title if self.movie else "Unknown Movie"
        user_name = self.user.username if self.user else "Unknown User"
        return f"Reservation for {movie_title} by {user_name}"

class SessionSeat(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat {self.seat.seat_number} in session {self.session.id}"
