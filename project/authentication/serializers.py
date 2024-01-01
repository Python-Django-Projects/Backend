from rest_framework import serializers
from .models import CustomUser
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email","username","password"]
    class CustomUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ["email","username","password","password_confirm"]
            
            # Add unique constraint to the phone field
            # extra_kwargs = {
            #     'phone': {'validators': []},
            #     'email': {'validators': []},
            # }


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ["email", "username", "password", "password_confirm"]

    def validate(self, data):
        """
        Ensure the passwords match.
        """
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data.
        """
        validated_data.pop('password_confirm', None)  # Remove password_confirm from the data
        user = get_user_model().objects.create_user(**validated_data)
        return user
