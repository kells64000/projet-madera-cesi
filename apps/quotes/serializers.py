from rest_framework import serializers
from .models import Quote


class QuoteListSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.CharField()
    attachment = serializers.CharField(allow_null=True, allow_blank=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Quote
        fields = ('id', 'name', 'phone', 'email', 'price', 'state',
                  'attachment', 'created_at', 'updated_at')

    def create(self, validated_data):
        """
        Create and return a new `Quote` instance, given the validated data.
        """
        return Quote.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.price = validated_data.get('price', instance.price)
        instance.state = validated_data.get('state', instance.state)
        instance.attachment = validated_data.get('attachment', instance.attachment)
        instance.save()
        return instance
