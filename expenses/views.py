from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def expenses_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expenses.html', {'expenses': expenses})

def expense_add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses:expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_add.html', {'form': form})

def expense_edit(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenses:expenses')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_edit.html', {'form': form, 'expense': expense})

def expense_delete(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expenses:expenses')
    return render(request, 'expenses/expense_delete.html', {'expense': expense})