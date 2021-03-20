from django.db import models
from datetime import datetime, timedelta

TYPES = [
    ('B', 'Bullet'),
    ('F', 'Food'),
    ('T', 'Travel'),
    ('S', 'Sport')
]
# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    description = models.CharField(max_length = 300)
    created_at = models.DateField()

class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=100)

class Journal(BookJournalBase):
    type = models.CharField(max_length = 100, choices=TYPES)
    publisher = models.CharField(max_length=200)