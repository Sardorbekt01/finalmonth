from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import *
from .serializers import*

class Customeroption(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class Productoption(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Categoryoption(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Itemoption(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer

class Shopcardoption(viewsets.ModelViewSet):
    queryset = Shopcart.objects.all()
    serializer_class = ShopcardSerializer

class CustomerPurchaseSummaryView(viewsets.ModelViewSet):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        purchases = PurchaseHistory.objects.filter(customer=customer)

        total_quantity = sum(purchase.quantity for purchase in purchases)
        total_amount = sum(purchase.total_price for purchase in purchases)

        response_data = {
            "Mijoz ismi": customer.f_name,
            "Haridlar soni": total_quantity,
            "Umumiy narx": total_amount
        }
        
        return Response(response_data, status=200)

