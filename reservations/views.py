from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation, WashingMachine
from .forms import ReservationForm
from datetime import datetime, timedelta
from django.shortcuts import redirect, get_object_or_404

def calendar_view(request):
    today = datetime.today().date()
    days = [today + timedelta(days=i) for i in range(14)]  # pokazuje tydzień
    return render(request, 'calendar.html', {'days': days})

@login_required
def day_view(request, date):
    # Pobierz wszystkie pralki
    date = datetime.strptime(date, "%Y-%m-%d").date()
    
    washing_machines = WashingMachine.objects.all()

    # Słownik przechowujący godziny rezerwacji dla każdej pralki
    reserved_hours_by_machine = {}

    for machine in washing_machines:
        # Pobierz wszystkie rezerwacje dla danej pralki na określoną datę
        reservations = Reservation.objects.filter(date=date, washing_machine=machine)

        # Stwórz słownik z godzinami jako kluczami i rezerwacjami jako wartościami
        reserved_hours = {}
        for reservation in reservations:
            hour = reservation.start_time.strftime("%H:%M")
            reserved_hours[hour] = {
                'username': reservation.user.username,
                'full_name': reservation.user.get_full_name(),
                'id': reservation.id
            }

        reserved_hours_by_machine[machine] = reserved_hours

    # Stwórz listę godzin, które chcesz wyświetlić
    hours = [(f"{hour:02d}:00", f"{hour:02d}:00-{hour+1:02d}:00") for hour in range(24)]

    print("Hours:", hours)

    return render(request, 'day.html', {
        'date': date,
        'hours': hours,
        'reserved_hours_by_machine': reserved_hours_by_machine,
        'washing_machines': washing_machines,
    })



@login_required
def reserve_view(request, date, hour, washing_machine_id):
    start_time = datetime.strptime(hour, "%H:%M").time()
    end_time = (datetime.strptime(hour, "%H:%M") + timedelta(hours=1)).time()
    washing_machine = WashingMachine.objects.get(id=washing_machine_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.date = date
            reservation.start_time = start_time
            reservation.end_time = end_time
            reservation.washing_machine = washing_machine
            reservation.save()
            return redirect('calendar')
    else:
        form = ReservationForm(initial={'date': date, 'start_time': start_time, 'end_time': end_time})

    return render(request, 'reserve.html', {'form': form, 'washing_machine': washing_machine})


@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # Sprawdź, czy użytkownik jest właścicielem rezerwacji lub jest administratorem
    if request.user == reservation.user or request.user.is_staff:
        reservation.delete()

    # Przekierowanie po usunięciu
    return redirect('day_view', date=reservation.date)
