from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'id')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'id',
            'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_custom_data(cls, user):
        custom_token_claim_attributes = dict()
        custom_user = User.objects.get(username=user.username)
        custom_token_claim_attributes['user_id'] = user.id
        custom_token_claim_attributes['username'] = user.username
        custom_token_claim_attributes['email'] = user.email

        return custom_token_claim_attributes

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        custom_token_claim_attributes =\
            LoginSerializer.get_custom_data(user)
        for key, value in custom_token_claim_attributes.items():
            token[key] = value
        return token
