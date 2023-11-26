from django.shortcuts import render, redirect, get_object_or_404
from .models import Income
from .forms import IncomeForm

def income(request):
    incomes = Income.objects.all()
    return render(request, 'income/income.html', {'incomes': incomes})

def income_add(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income:income')
    else:
        form = IncomeForm()
    return render(request, 'income/income_add.html', {'form': form})

def income_edit(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('income:income')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'income/income_edit.html', {'form': form, 'income': income})

def income_delete(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        income.delete()
        return redirect('income:income')
    return render(request, 'income/income_delete.html', {'income': income})
