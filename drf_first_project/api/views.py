from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloApiView(APIView):
    def get(self, request):
        data={
            'message': 'Hello World',
            'status': 'success',
            "learning": "DRF Day 1"
        }
        return Response(data, status=status.HTTP_200_OK)

