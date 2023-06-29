from rest_framework import serializers
from .models import FormEntry

class FormEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FormEntry
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def validate_email(self, value):
        # Perform email validation
        # Implement your own email validation logic here
        if not value.endswith('@example.com'):
            raise serializers.ValidationError('Invalid email domain.')
        return value

    def validate_phone_number(self, value):
        # Perform phone number validation
        # Implement your own phone number validation logic here
        if len(value) != 10:
            raise serializers.ValidationError('Phone number must be 10 digits.')
        return value
