from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee # Specify the model to be serilaized
        fields = ['id', 'name', 'age', 'salary', 'phone_number', 'location'] 