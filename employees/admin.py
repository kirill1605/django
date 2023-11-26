from django.contrib import admin
from .models import Employee
from import_export.admin import ImportExportMixin

class EmployeeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'age', 'salary', 'get_orders_count')
    list_filter = ('position', 'age')
    inlines = []
    date_hierarchy = 'date'
    search_fields = ('first_name', 'last_name', 'position')
    filter_horizontal = ()
    list_display_links = ('first_name', 'last_name')
    raw_id_fields = ()
    readonly_fields = ()

    def get_orders_count(self, obj):
        return obj.orders.count()
    get_orders_count.short_description = 'Количество заказов'

admin.site.register(Employee, EmployeeAdmin)