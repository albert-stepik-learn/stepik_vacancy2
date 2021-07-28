from django import forms

from vacancy.models import Company, Vacancy


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'location', 'logo', 'description', 'employee_count']


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ['title', 'speciality', 'skills', 'description', 'salary_min', 'salary_max']
