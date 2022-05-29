from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ticket


@login_required
def tickets_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticketslist.html', {'title': 'Tickets list', 'tickets': tickets})



