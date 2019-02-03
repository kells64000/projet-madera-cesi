from rest_framework import serializers
from .models import Quote


class QuoteListSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Quote
        fields = ('id', 'name', 'phone', 'email', 'price', 'state', 'created_at', 'updated_at')
