from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    movie = models.CharField(max_length=100, default="Source Code")
    venue = models.CharField(max_length=100, default="APJ Hall")
    time = models.CharField(max_length=50, default="4:30 PM")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.movie}'
