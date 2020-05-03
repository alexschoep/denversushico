from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm
from django.views.generic.detail import DetailView
from .sendEmail import EmailMessage


# Create your views here.

#displays the landing page
def index(request):
    return render(request, 'index.html')


def reserve(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            # email = EmailMessage(reservation)
            # email.send()
            return redirect('view', pk=reservation.url)

    else:
        form = ReservationForm()
    
    context = {"form": form}
    return render(request, 'reserve.html', context)


class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'view.html'


def edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('view', pk=pk)

    else:
        form = ReservationForm(initial={'name': reservation.name, 'email': reservation.email, 'date': reservation.date, 
                                    'time': reservation.time, 'partySize': reservation.partySize, 'notes': reservation.notes})
    context = {
        "reservation": reservation,
        "form": form
    }
    return render(request, 'edit.html', context)
