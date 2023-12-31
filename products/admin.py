from django.contrib import admin
from .models import Product
from import_export import resources
from import_export.admin import ImportExportMixin


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

    def get_user(self, product):
        user = product.user
        return user.username if user else ""

    def dehydrate_user(self, product):
        return self.get_user(product)

class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("name", "description", "price", "get_discounted_price")
    list_filter = ("price",)
    inlines = []
    date_hierarchy = "date"
    search_fields = ("name", "description")
    filter_horizontal = ()
    list_display_links = ("name",)
    raw_id_fields = ()
    readonly_fields = ()

    def get_discounted_price(self, obj):
        return float(obj.price) * 0.9

    get_discounted_price.short_description = "Со скидкой"


admin.site.register(Product, ProductAdmin)
