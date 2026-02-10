from django.urls import path
from .views import CustomerListAPIView

urlpatterns = [
    path('customerlist/', CustomerListAPIView.as_view()),
]