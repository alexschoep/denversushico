from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def reserve(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('view', resid=reservation.id)
        else:
            print('invalid form submission')

    form = ReservationForm()
    context = {
        "form": form
    }
    return render(request, 'reserve.html', context)


def view(request, resid):
    reservation = get_object_or_404(Reservation, pk=resid)
    return render(request, 'view.html', {'reservation': reservation})


def edit(request, resid):
    reservation = get_object_or_404(Reservation, pk=resid)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('view', resid=resid)

    form = ReservationForm(initial={'name': reservation.name, 'phoneNum': reservation.phoneNum, 'email': reservation.email,
                                    'date': reservation.date, 'time': reservation.time, 'partySize': reservation.partySize, 'notes': reservation.notes})
    context = {
        "reservation": reservation,
        "form": form
    }
    return render(request, 'edit.html', context)
