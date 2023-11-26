from django.contrib import admin
from .models import Income

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('operation_name', 'payment_method', 'amount', 'custom_method')
    list_filter = ('payment_method',)
    inlines = []
    date_hierarchy = 'date'
    
    @admin.display(description='Custom Method')
    def custom_method(self, obj):
        return obj.custom_field
    
    custom_method.short_description = 'Custom Field'
    
    filter_horizontal = ()
    list_display_links = None
    raw_id_fields = ()
    readonly_fields = ()
    search_fields = ('operation_name',)\

admin.site.register(Income, IncomeAdmin)
