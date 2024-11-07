from rest_framework import serializers

from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"



class UserSerializer(serializers.ModelSerializer):

    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class UserLightSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            "password",
            "last_name",
        )
