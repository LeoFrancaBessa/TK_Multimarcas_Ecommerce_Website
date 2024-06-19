from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from .utils import generate_random_string

User = get_user_model()

class SignupSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True, required = True)
    first_name = serializers.CharField(write_only=True, required = True)
    last_name = serializers.CharField(write_only=True, required = True)
    password1 = serializers.CharField(write_only=True, required = True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required = True)

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'password':"Password fields didn't match."})
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email':"Email already exists."})
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['email'][:20] + generate_random_string(9),
            email=validated_data['email'],
            password = validated_data['password1'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user