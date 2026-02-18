from django.urls import path
from .views import (StudentProListCreateAPIView, StudentProRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('studentpro/', StudentProListCreateAPIView.as_view()),
    path('studentpro/<int:pk>/', StudentProRetrieveUpdateDestroyAPIView.as_view()),
]