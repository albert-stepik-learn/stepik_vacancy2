from django.db import models


class Speciality(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

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

    def clean(self):
        if self.salary_max < self.salary_min:
            raise ValueError({
                'salary_min': ValueError('"salary_max" must not be less than "salary_min"'),
                'salary_max': ValueError('"salary_max" must not be less than "salary_min"'),
            })
