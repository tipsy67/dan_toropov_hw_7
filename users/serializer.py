from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    payments = PaymentSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"
