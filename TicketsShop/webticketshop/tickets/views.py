import asyncio

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tickets
from .forms import TicketForm
from asgiref.sync import sync_to_async
import logging

logger = logging.getLogger(__name__)


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
            logger.info('Ticket updated')
        return render(request, 'tickets/create.html', {'form': form})
    else:
        if id == 0:
            form = TicketForm(request.POST)
        else:
            tickets = Tickets.objects.get(pk=id)
            form = TicketForm(request.POST, instance=tickets)
        if form.is_valid():
            logger.info('Ticket added')
            form.save()
        return redirect('/main/tickets')


@login_required
def delete(request, id):
    asyncio.run(async_tasks(id))
    return redirect('/main/tickets')


async def async_tasks(id):
    task1 = asyncio.create_task(delete_ticket(id))
    task2 = asyncio.create_task(print_log(id))
    await asyncio.gather(task1, task2)


@sync_to_async
def delete_ticket(id):
    tickets = Tickets.objects.get(pk=id)
    tickets.delete()


@sync_to_async
def print_log(id):
    logger.info("ticket ", id)