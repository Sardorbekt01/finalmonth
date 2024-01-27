from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('product', Productoption, basename='product')
router.register('category', Categoryoption, basename='category')
router.register('customer', Customeroption, basename='customer')
router.register('item',Itemoption, basename='item')
router.register('shopcard',Shopcardoption, basename='shopcard')
router.register('purchase',CustomerPurchaseSummaryView, basename='purchase')

urlpatterns = router.urls

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls