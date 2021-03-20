from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.permissions import *

from .serializers import *


# Create your views here.

class BookAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


class JournalAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


class JournalRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = JournalSerializer

    def get_queryset(self):
        return Journal.objects.all()

