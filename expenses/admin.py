from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'operation_name', 'amount', 'custom_method')
    list_filter = ('date',)
    inlines = []
    date_hierarchy = 'date'
    filter_horizontal = ()
    list_display_links = ('id', 'operation_name')
    raw_id_fields = ()
    readonly_fields = ('date',)
    search_fields = ('operation_name',)

    def custom_method(self, obj):
        return obj.custom_field
    
    custom_method.short_description = 'Custom Field'

admin.site.register(Expense, ExpenseAdmin)
