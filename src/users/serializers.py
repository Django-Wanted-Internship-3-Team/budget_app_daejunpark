from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer


class UserSignUpSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        raw_password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(raw_password)
        user.save()
        return user
