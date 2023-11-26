from django.contrib import admin
from .models import Order, OrderEmployee
from django import forms
from employees.models import Employee


class OrderEmployeeInline(admin.TabularInline):
    model = OrderEmployee


class OrderEmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee', 'order',)
    list_filter = ('employee', 'order')
    inlines = []
    date_hierarchy = 'date'
    list_display_links = ('employee', 'order')
    raw_id_fields = ()
    readonly_fields = ()
    search_fields = ('employee__first_name', 'employee__last_name', 'order__product_name')


admin.site.register(OrderEmployee, OrderEmployeeAdmin)


class OrderForm(forms.ModelForm):
    employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('employees', is_stacked=False),
        required=False,
        label='Employees'
    )

    class Meta:
        model = Order
        fields = '__all__'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'delivery_address', 'get_employees_names', 'price',)
    list_filter = ('price',)
    inlines = [OrderEmployeeInline]
    date_hierarchy = 'date'
    list_display_links = ('product_name',)
    readonly_fields = ('get_employees_names',)
    filter_horizontal = ('employees',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        employees = form.cleaned_data.get('employees')
        if employees is not None:
            for employee in employees:
                OrderEmployee.objects.update_or_create(
                    order=obj,
                    employee=employee,
                )

    def get_employees_names(self, obj):
        return ', '.join([str(employee) for employee in obj.employees.all()])
    get_employees_names.short_description = 'Сотрудники'


