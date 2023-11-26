from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees:employees')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees:employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees:employees')
    return render(request, 'employees/delete_employee.html', {'employee': employee})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employees.html', {'employees': employees})



class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer