from django.contrib import admin
from product.models import ProductTable


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = ProductTable


admin.site.register(ProductTable, ProductAdmin)
