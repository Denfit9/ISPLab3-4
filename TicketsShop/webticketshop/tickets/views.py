from django.shortcuts import render


# Create your views here.
def tickets_list(request):
    return render(request, 'tickets/ticketslist.html')
