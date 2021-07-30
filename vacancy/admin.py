from django.contrib import admin

# Register your models here.
from vacancy.models import Company, Vacancy, Resume


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'logo', 'description', 'employee_count', 'owner']
    search_fields = ['name']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'speciality', 'skills', 'description', 'salary_min', 'salary_max', 'published_at',
                    'company']
    search_fields = ['title']


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'status', 'salary', 'speciality', 'grade', 'education', 'experience',
                    'portfolio']
    search_fields = ['name']
