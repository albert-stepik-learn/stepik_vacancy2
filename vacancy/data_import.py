"""Import data from data.py to ORM models
"""
import os


import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'stepik_vacancy2.settings'
django.setup()

from django.contrib.auth.models import User

from vacancy.models import Vacancy, Company, Speciality, Application
from vacancy import data


for company_data in data.companies:
    admin = User.objects.get(pk=1)
    Company.objects.create(
        id=company_data['id'],
        name=company_data['title'],
        logo=f"vacancy/static/vacancy/{company_data['logo']}",
        employee_count=company_data['employee_count'],
        location=company_data['location'],
        description=company_data['description'],
        owner=admin,
    )

for speciality_data in data.specialties:
    Speciality.objects.create(
        code=speciality_data['code'],
        title=speciality_data['title'],
        logo=f"vacancy/static/vacancy/specty_{speciality_data['code']}.png"
    )

for vacancy_data in data.jobs:
    Vacancy.objects.create(
        id=vacancy_data['id'],
        title=vacancy_data['title'],
        speciality=Speciality.objects.get(code=vacancy_data['specialty']),
        company=Company.objects.get(id=vacancy_data['company']),
        salary_min=vacancy_data['salary_from'],
        salary_max=vacancy_data['salary_to'],
        published_at=vacancy_data['posted'],
        skills=vacancy_data['skills'],
        description=vacancy_data['description'],
    )
