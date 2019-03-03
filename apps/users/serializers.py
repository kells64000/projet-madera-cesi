from rest_framework import serializers
from addresses.models import Address
from addresses.serializers import AddressSerializer
from .models import MaderaUser, SalesPerson, Client


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MaderaUserSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    full_name = serializers.SerializerMethodField()
    phone = serializers.CharField(required=False, allow_blank=True, max_length=12)
    address = AddressSerializer()

    date_joined = serializers.DateTimeField(required=False)
    is_active = serializers.BooleanField(required=False)
    is_staff = serializers.BooleanField(default=False)

    class Meta:
        model = MaderaUser
        fields = ('id', 'email', 'first_name', 'last_name', 'full_name', 'phone',
                  'address', 'date_joined', 'is_active', 'is_staff')
        write_only_fields = ('password',)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        user = MaderaUser.objects.create(
            address=Address.objects.create(**address_data),
            **validated_data)
        return user

    def to_representation(self, obj):
        """Exclude password from returning dict"""
        ret = super(MaderaUserSerializer, self).to_representation(obj)
        ret.pop('password', None)
        return ret

    def get_full_name(self, obj):
        return obj.get_full_name


class SalesPersonSerializer(MaderaUserSerializer):

    workplace = serializers.CharField(required=True, allow_blank=False, max_length=50)

    class Meta(MaderaUserSerializer.Meta):
        model = SalesPerson
        fields = MaderaUserSerializer.Meta.fields + ('workplace',)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        salesperson = SalesPerson.objects.create(
            address=Address.objects.create(**address_data),
            **validated_data)
        return salesperson


class ClientSerializer(MaderaUserSerializer):

    is_pro = serializers.BooleanField()
    company = serializers.CharField(required=False, allow_blank=True, max_length=50)

    class Meta(MaderaUserSerializer.Meta):
        model = Client
        fields = MaderaUserSerializer.Meta.fields + ('is_pro', 'company')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        client = Client.objects.create(
            address=Address.objects.create(**address_data),
            **validated_data)
        return client
