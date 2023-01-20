from django.contrib import admin
from shop.models import Product, Tag

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','description')

admin.site.register(Product, ProductAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Tag, TagAdmin)
