from rest_framework import serializers
from .models import Customer
import phonenumbers
import re

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

    def validate_phone_number(self, value):
        try:
            parsed_number = phonenumbers.parse(value, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise serializers.ValidationError("Invalid phone number.")
            if phonenumbers.number_type(parsed_number) != phonenumbers.PhoneNumberType.MOBILE:
                raise serializers.ValidationError("The phone number must be a valid mobile number.")
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Invalid phone number.")
        customer_id = self.instance.id if self.instance else None
        if Customer.objects.exclude(id=customer_id).filter(phone_number=value).exists():
            raise serializers.ValidationError("Phone number must be unique.")
        return value

    def validate_bank_account_number(self, value):
        if not re.match(r'^\d{10,15}$', value):
            raise serializers.ValidationError("Bank account number must be between 10 and 15 digits.")
        customer_id = self.instance.id if self.instance else None
        if Customer.objects.exclude(id=customer_id).filter(bank_account_number=value).exists():
            raise serializers.ValidationError("Bank account number must be unique.")
        return value

    def validate_email(self, value):
        customer_id = self.instance.id if self.instance else None
        if Customer.objects.exclude(id=customer_id).filter(email=value).exists():
            raise serializers.ValidationError("Email must be unique.")
        return value
