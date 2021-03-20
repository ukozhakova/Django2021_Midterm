from rest_framework import serializers

from api.models import BookJournalBase, Book, Journal


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'



class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
