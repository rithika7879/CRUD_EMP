from django.contrib import admin
from django.urls import path,include
from emp.views import employee,EmployeeView

from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    
    path('employee/', employee, name='employee'),
    path('employee/', EmployeeView.as_view(), name='employee')
    
]+router.urls
