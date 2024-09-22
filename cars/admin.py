from django.contrib import admin
from cars.models import car
from cars.models import car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model','brand')
    

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
admin.site.register(car, CarAdmin)
admin.site.register(Brand, BrandAdmin)