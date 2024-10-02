from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Ticket

@csrf_exempt
def create_ticket(request):
    if request.method == 'POST':
        # Safely get the form data using request.POST.get()
        name = request.POST.get('name', None)
        branch = request.POST.get('branch', None)
        phone = request.POST.get('phone', None)
        print(name)
        # Check if any field is missing
        if not all([name, branch, phone]):
            return render(request, 'index.html', {'error': 'All fields are required'})

        # Create a new ticket entry
        ticket = Ticket(name=name, branch=branch, phone=phone)
        ticket.save()

        # Pass the ticket data to the template to render
        context = {
            'name': name,
            'branch': branch,
            'phone': phone,
            'ticket_id': ticket.id
        }

        # Render the ticket details page
        return render(request, 'ticket.html', context)
    else:
        return render(request, 'index.html')
