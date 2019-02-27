from rest_framework import serializers
from .models import Quote


class QuoteListSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.CharField()
    attachment = serializers.CharField(allow_null=True, allow_blank=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    customer = serializers.SerializerMethodField()
    salesman = serializers.SerializerMethodField()

    class Meta:
        model = Quote
        fields = ('id', 'customer', 'salesman' 'price', 'state',
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
        instance.customer = validated_data.get('customer', instance.customer)
        instance.salesman = validated_data.get('salesman', instance.salesman)
        instance.price = validated_data.get('price', instance.price)
        instance.state = validated_data.get('state', instance.state)
        instance.attachment = validated_data.get('attachment', instance.attachment)
        instance.save()
        return instance
