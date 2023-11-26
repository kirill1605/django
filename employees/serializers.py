from rest_framework import serializers
from rest_framework import viewsets
from django.db.models import Q
from .models import Employee
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'position', 'salary')


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(
        Q(salary__gt=50000)
        | Q(first_name__startswith="В")
    )

    @action(methods=['GET'], detail=False)
    def get_high_salary_employees(self, request):
        # Get employees with salary greater than 50000
        high_salary_employees = self.get_queryset().filter(salary__gt=50000)

        # Serialize the employees
        serialized_employees = EmployeeSerializer(high_salary_employees, many=True)

        # Return the serialized employees
        return Response(serialized_data=serialized_employees.data)

    @action(methods=['POST'], detail=True)
    def update_salary(self, request, pk):
        employee = self.get_object()
        new_salary = request.data["salary"]

        employee.salary = new_salary
        employee.save()

        serialized_employee = EmployeeSerializer(employee)
        return Response(serialized_data=serialized_employee.data)