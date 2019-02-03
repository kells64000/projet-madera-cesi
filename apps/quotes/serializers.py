from rest_framework import serializers
from .models import Quote

class QuoteListSerializer(serializers.ModelSerializer):

    id = serializers.AutoField(primary_key=True)
    name = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.TextField()
    created_at = serializers.DateTimeField(auto_now_add=True)
    updated_at = serializers.DateTimeField(auto_now=True)

class Meta:
    model = Quote
    fields = ('id', 'name', 'phone', 'email', 'price', 'state', 'created_at', 'updated_at')