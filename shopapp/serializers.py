from rest_framework import serializers
from .models  import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email

        return token

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ShopcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopcart
        fields = '__all__'

class ItemSerializer(serializers.Serializer):
    class Meta:
        model = Items
        fields = '__all__'

class PurchaseHistorySerializer(serializers.Serializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'

