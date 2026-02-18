from rest_framework import generics
from .models import StudentPro
from .serializers import StudentProSerializer

# Create your views here.

class StudentProListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentPro.objects.all()
    serializer_class = StudentProSerializer


class StudentProRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentPro.objects.all()
    serializer_class = StudentProSerializer
