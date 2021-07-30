"""stepik_vacancy1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf.urls.static import static

from stepik_vacancy2 import settings
from vacancy import views
from vacancy.views import CompanyDetailView, CompanyListView, SpecialityDetailView, VacancyDetailView, \
    VacancyListView, ApplicationCreateView, company_lets_start_view, MyCompanyEditView, MyVacancyListView, \
    MyVacancyDetailView, MyVacancyCreateView, MySignupView, MyLoginView, MyCompanyCreateView, ResumeView, \
    ResumeCreateView, resume_lets_start_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='main'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company'),
    path('companies/', CompanyListView.as_view(), name='companies'),
    path('vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy'),
    path('vacancies/<int:vacancy_id>/send/', ApplicationCreateView.as_view(), name='application'),
    path('vacancies/cat/<str:code>/', SpecialityDetailView.as_view(), name='speciality'),
    path('mycompany/', MyCompanyEditView.as_view(), name='company_edit'),
    path('mycompany/letsstart/', company_lets_start_view, name='lets_start'),
    path('mycompany/create/', MyCompanyCreateView.as_view(), name='company_create'),
    path('mycompany/vacancies/', MyVacancyListView.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/<int:vacancy_id>/', MyVacancyDetailView.as_view(), name='my_vacancy'),
    path('mycompany/vacancies/create/', MyVacancyCreateView.as_view(), name='my_vacancy_create'),
    path('myresume/letsstart/', resume_lets_start_view, name='myresume_start'),
    path('myresume/create/', ResumeCreateView.as_view(), name='myresume_create'),
    path('myresume/', ResumeView.as_view(), name='myresume'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),   # settings.LOGOUT_REDIRECT_URL = '/login/'
    path('signup/', MySignupView.as_view(), name='signup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
