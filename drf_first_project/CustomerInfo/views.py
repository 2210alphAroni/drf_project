from rest_framework import viewsets
from .models import CustomerInfo
from .serializers import CustomerInfoSerializer

# Create your views here.

class CustomerInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all().order_by('-id') # ordering by id in descending order
    serializer_class = CustomerInfoSerializer
