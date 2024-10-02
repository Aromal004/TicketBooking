from django.contrib import admin
from .models import Ticket

# Register the Ticket model to the admin panel
class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'movie', 'venue', 'time', 'created_at')
    search_fields = ('name', 'phone', 'movie')
    list_filter = ('movie', 'venue', 'time')
    ordering = ('-created_at',)

admin.site.register(Ticket, TicketAdmin)
