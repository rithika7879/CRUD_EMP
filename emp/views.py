from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

def employee(request):
    
    if request.method == 'GET':
        objEmployee = Employee.objects.all()
        serializer = EmployeeSerializer(objEmployee, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = EmployeeSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        data = request.data
        try:
            obj = Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        serializer = EmployeeSerializer(obj, data=data, partial=False)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'PATCH':
        data = request.data
        try:
            obj = Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        serializer = EmployeeSerializer(obj, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        data = request.data
        try:
            obj = Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        obj.delete()
        return Response({"message": "Employee deleted successfully"}, status=204)
    

# Class based

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            employee = Employee.objects.get(id=request.data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            employee = Employee.objects.get(id=request.data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(Employee, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            employee = Employee.objects.get(id=request.data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        employee.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    


from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()  # Define the queryset for the viewset
    serializer_class = EmployeeSerializer  # Specify the serializer to be used


        
    
