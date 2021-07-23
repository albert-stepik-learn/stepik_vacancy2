from django.contrib import admin

# Register your models here.
from vacancy.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'logo', 'description', 'employee_count', 'owner']
    search_fields = ['name']
