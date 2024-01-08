from rest_framework import serializers
from rest_framework import viewsets
from .models import Employee
from rest_framework.decorators import action

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'position', 'salary')

    def validate_first_name(self, value):
        if value is None:
            raise serializers.ValidationError("Введите имя")
        return value

    def validate_last_name(self, value):
        if value is None:
            raise serializers.ValidationError("Введите фамилию")
        return value

    def validate_salary(self, value):
        if value is None:
            raise serializers.ValidationError("Введите сумму ЗП")
        return value

    def validate_position(self, value):
        if value is None:
            raise serializers.ValidationError("Введите должность")
        return value


class EmployeeViewSet(viewsets.ModelViewSet):


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