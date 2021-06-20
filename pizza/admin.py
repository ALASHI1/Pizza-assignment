from django.contrib import admin
from .models import *
# Register your models here.
class PizzaVaultAdmin(admin.ModelAdmin):
	list_display = ('types','size','toppings')


admin.site.register(PizzaVault,PizzaVaultAdmin)