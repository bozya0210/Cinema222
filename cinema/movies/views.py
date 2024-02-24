from django.shortcuts import render, get_object_or_404
from .models import Movie, Seat, Reservation, Session, SessionSeat
from django.utils import timezone
from django.http import HttpResponseRedirect
def movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movies_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})




# def booking_page(request, movie_id, session_id):
#     # Ваш код для обработки страницы бронирования сеанса
#     return HttpResponse(f"Вы находитесь на странице бронирования фильма {movie_id} для сеанса {session_id}")
def show_seats_selection(request, movie_id, session_id):
    # Получаем места только для выбранного сеанса
    session_seats = SessionSeat.objects.filter(session_id=session_id, is_reserved=False)
    return render(request, 'movies/seats_selection.html', {'session_seats': session_seats, 'session_id': session_id})



def process_seats_selection(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        selected_seats = request.POST.getlist('selected_seats')
        for seat_id in selected_seats:
            session_seat = SessionSeat.objects.get(session_id=session_id, seat_id=seat_id)
            session_seat.is_reserved = True
            session_seat.save()

            # Создание записи в таблице Reservation
            reservation = Reservation()
            reservation.movie_session = Session.objects.get(id=session_id)
            reservation.seat = session_seat.seat
            reservation.user_name = request.user.name  # Или любое другое значение, которое вы хотите использовать
            reservation.user_email = request.user.email  # Или любое другое значение, которое вы хотите использовать
            reservation.reservation_time = timezone.now()  # Импортировать: from django.utils import timezone
            reservation.save()

        return HttpResponseRedirect('/success/')  # Перенаправление на страницу успешного бронирования
    return HttpResponseRedirect('/error/')  # Перенаправление на страницу ошибки

