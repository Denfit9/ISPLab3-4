from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tickets
from .forms import TicketForm


@login_required
def tickets_list(request):
    tickets = Tickets.objects.order_by('-id')
    return render(request, 'tickets/ticketslist.html', {'title': 'Tickets list', 'tickets': tickets})


@login_required
def create(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = TicketForm()
        else:
            tickets = Tickets.objects.get(pk=id)
            form = TicketForm(instance=tickets)
        return render(request, 'tickets/create.html', {'form': form})
    else:
        if id == 0:
            form = TicketForm(request.POST)
        else:
            tickets = Tickets.objects.get(pk=id)
            form = TicketForm(request.POST, instance=tickets)
        if form.is_valid():
            form.save()
        return redirect('/main/tickets')


@login_required
def delete(request, id):
    tickets = Tickets.objects.get(pk=id)
    tickets.delete()
    return redirect('/main/tickets')
