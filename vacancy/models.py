from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from stepik_vacancy2.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR

class Speciality(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR, height_field='height_field', width_field='width_field')
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, related_name='company')

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=200)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=120)
    written_phone = models.CharField(max_length=15)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "applications")


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)

    NOTREADY = 'NR'
    READYTOOFFER = 'RF'
    READYTOWORK = 'RW'

    READYNESS_STATUS_CHOICES = [
        (NOTREADY, 'Не ищу работу'),
        (READYTOOFFER, 'Рассматриваю предложения'),
        (READYTOWORK, 'Ищу работу'),
    ]

    status = models.CharField(
        max_length=2,
        choices=READYNESS_STATUS_CHOICES,
        default=NOTREADY,
    )
    salary = models.IntegerField()
    speciality = models.CharField(max_length=120)

    INTERN = 'IN'
    JUNIOR = 'JN'
    MIDDLE = 'MD'
    LEED = 'LD'

    GRADE_CHOICES = [
        (INTERN, 'Стажер'),
        (JUNIOR, 'Младший разработчик'),
        (MIDDLE, 'Разработчик'),
        (LEED, 'Ведущий разработчик'),
    ]

    grade = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES,
        default=INTERN,
    )
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.URLField(max_length=200)

    def __str__(self):
        print(self.name)