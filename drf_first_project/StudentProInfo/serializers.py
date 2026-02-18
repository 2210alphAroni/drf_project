from rest_framework import serializers
from .models import StudentPro

class StudentProSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPro
        fields = '__all__'