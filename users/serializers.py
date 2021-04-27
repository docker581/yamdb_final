from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        ]
        model = User
        extra_kwargs = {
            'password': {'required': False},
            'email': {'required': True}
        }


class TokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField()

    def validate(self, data):
        email = data['email']
        confirmation_code = data['confirmation_code']
        user = User.objects.filter(
            email=email,
            confirmation_code=confirmation_code,
        ).first()
        if user is None:
            raise serializers.ValidationError(
                {'detail': 'Validation error!'})
        token = {'token': str(AccessToken.for_user(user))}
        return token
