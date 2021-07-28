from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from vacancy.models import Company, Vacancy


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'location', 'logo', 'description', 'employee_count']


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ['title', 'speciality', 'skills', 'description', 'salary_min', 'salary_max']


class MySignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput,
        # help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        strip=False,
        widget=forms.PasswordInput,
        # help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password': 'Пароль',
        }
