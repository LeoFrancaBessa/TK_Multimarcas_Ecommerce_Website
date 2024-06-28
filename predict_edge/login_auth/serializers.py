from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from .utils import generate_random_string, validate_email

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required = True)
    password = serializers.CharField(write_only=True, required = True)

    def validate(self, attrs):
        if not attrs['username']:
            raise serializers.ValidationError({"message" : "Informe seu usuário."})
        if not attrs['password'] not in attrs:
            raise serializers.ValidationError({"message" : "Informe sua senha."})
        return super().validate(attrs)


class SignupSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True, required = True)
    name = serializers.CharField(write_only=True, required = True)
    password1 = serializers.CharField(write_only=True, required = True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required = True)

    def validate(self, attrs):
        if len(attrs['password1']) < 8 or len(attrs['password2']) < 8:
            raise serializers.ValidationError({'message':"Senhas precisam ter 8 caracteres ou mais."})
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'message':"Senhas não correspondem."})
        if not validate_email(attrs['email']):
            raise serializers.ValidationError({'message':"Email digitado não é valido."})
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'message':"Email já cadastrado."})
        return super().validate(attrs)
    
    def create(self, validated_data):
        first_name = validated_data['name'].split(' ')[0]
        last_name = ' '.join(validated_data['name'].split(' ')[1:])

        user = User.objects.create_user(
            username =validated_data['email'][:20] + generate_random_string(9),
            email=validated_data['email'],
            password =validated_data['password1'],
            first_name=first_name,
            last_name=last_name,
        )
        return user