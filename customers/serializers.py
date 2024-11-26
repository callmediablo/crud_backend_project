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
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Invalid phone number.")
        return value
    
    def validate_bank_account_number(self, value):
        if not re.match(r'^\d{10,15}$', value):
            raise serializers.ValidationError("Bank account number must be between 10 and 15 digits.")
        return value