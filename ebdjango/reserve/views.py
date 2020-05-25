from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import MakeReservationForm, EditReservationForm
from django.views.generic.detail import DetailView
from .sendEmail import sendEmail

# Create your views here.

#displays the landing page
def index(request):
    form = MakeReservationForm()
    context = {
        "formAction": '/reserve/',
        "initial": True,
        "form": form
    }
    return render(request, 'index.html', context)


def reserve(request):
    if request.method == "POST":
        form = MakeReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            sendEmail(reservation)
            return redirect('view', pk=reservation.url)

    else:
        form = MakeReservationForm()
    
    context = {
        "formAction": '',
        "initial": True,
        "form": form
    }
    return render(request, 'reserve.html', context)


class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'view.html'


def edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    
    if request.method == "POST":
        form = EditReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('view', pk=pk)

    else:
        form = EditReservationForm(initial={'name': reservation.name, 'date': reservation.date, 
                                    'time': reservation.time, 'partySize': reservation.partySize, 'notes': reservation.notes})

    context = {
        "formAction": '',
        "initial": False,
        "reservation": reservation,
        "form": form
    }
    return render(request, 'edit.html', context)


def delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        reservation.delete()
    return redirect('reserve')
