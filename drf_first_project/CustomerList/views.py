from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CustomerListAPIView(APIView):
    def get(self, request):
        customers = [
            {"id": 1, "name": "John Doe", "email": "john@example.com"},
            {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
        ]
        return Response(customers, status=status.HTTP_200_OK)