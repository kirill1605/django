from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Employee
from .serializers import EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employees:employees")
    else:
        form = EmployeeForm()
    return render(request, "employees/add_employee.html", {"form": form})


def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employees:employees")
    else:
        form = EmployeeForm(instance=employee)
    return render(
        request, "employees/edit_employee.html", {"form": form, "employee": employee}
    )


def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == "POST":
        employee.delete()
        return redirect("employees:employees")
    return render(request, "employees/delete_employee.html", {"employee": employee})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employees/employees.html", {"employees": employees})

class EmployeeAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        "salary"
    ]
    search_fields = [
        "first_name",
        "last_name",
    ]
    ordering_fields = [
        'first_name'
    ]

    def get_queryset(self):
        user = self.request.user

        queryset = Employee.objects.filter(user=user)

        queryset = queryset.filter(Q(salary__gt=50000) | (Q(first_name__startswith = 'П') | ~ Q(first_name__startswith = 'С')))

        return queryset

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=['GET'])
    def get_high_salary_employees(self, request):
        high_salary_employees = Employee.objects.filter(salary__gt=50000)
        serialized_employees = self.get_serializer(high_salary_employees, many=True)
        return Response(data=serialized_employees.data)

    @action(detail=True, methods=['POST'])
    def update_salary(self, request, pk):
        employee = self.get_object()
        new_salary = request.data.get("salary")

        if new_salary is not None:
            employee.salary = new_salary
            employee.save()
            serialized_employee = self.get_serializer(employee)
            return Response(data=serialized_employee.data)
        else:
            return Response(data={"error": "Salary is required"}, status=status.HTTP_400_BAD_REQUEST)