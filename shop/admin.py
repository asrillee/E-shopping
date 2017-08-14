from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from .models import Inventory, Cart

# Register your models here.

# class MyAdminSite(AdminSite):
#     site_header = 'Herbology'
#     site_title = 'Site Admin'
#
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('item_no', 'item_name', 'item_category', 'item_image', 'user')
    list_filter = ('item_name',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart_no', 'inventory', 'quantity', 'user')
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'is_active', 'is_staff', 'is_superuser')

# admin_site = MyAdminSite(name='herbology_admin')

# admin_site.register(User, UserAdmin)
# admin_site.register(Group)
# admin_site.register(Inventory, InventoryAdmin)

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Cart, CartAdmin)