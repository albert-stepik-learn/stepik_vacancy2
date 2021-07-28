from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .forms import CompanyForm, VacancyForm, MySignUpForm
from .models import Company, Speciality, Vacancy, Application


# Landing page with companies and categories:
def main_view(request):
    print(f'Request: {request.GET}')
    return render(
        request,
        'vacancy/index.html',
        context={
            'specialities': Speciality.objects.annotate(vacancy_count=Count('vacancies')),
            'companies': Company.objects.annotate(vacancy_count=Count('vacancies')),
        },
    )


# All vacancies:
class VacancyListView(ListView):
    model = Vacancy


# Details on a specified vacancy:
class VacancyDetailView(DetailView):
    model = Vacancy


# Vacancies of a specified speciality (category):
class SpecialityDetailView(DetailView):
    model = Speciality
    slug_field = 'code'
    slug_url_kwarg = 'code'

    def get_context_data(self, **kwargs):
        context = super(SpecialityDetailView, self).get_context_data(**kwargs)
        context['vacancy_list'] = Vacancy.objects.filter(speciality_id=self.object.pk)
        return context


# A list of companies:
class CompanyListView(ListView):
    model = Company


# Company and its vacations:
class CompanyDetailView(DetailView):
    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['vacancy_list'] = Vacancy.objects.filter(company__id=self.object.pk)
        return context


# Apply for a vacation:
class ApplicationDetailView(DetailView):
    model = Application


# Propose a new company creation:
def lets_start_view(request):
    return render(request, 'vacancy/lets-start.html', context={})


# Create a company:
class MyCompanyCreateView(LoginRequiredMixin, CreateView):
    def get(self, request, *args):
        return render(request, 'vacancy/company-create.html', context={'form': CompanyForm})

    def post(self, request, *args):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner_id = request.user.id
            company.save()
            return redirect('/mycompany/')
        return render(request, 'vacancy/company-create.html', context={'form': form})


# View and edit a company:
class MyCompanyEditView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args):
        owner_id = request.user.id
        company = Company.objects.filter(owner__id=owner_id).first()
        if not company:
            return redirect('/mycompany/letsstart/')
        else:
            form = CompanyForm(instance=company)
            return render(request, 'vacancy/mycompany.html/', context={'form': form, 'company_name': company.name})

    def post(self, request):
        print(request.POST)
        owner_id = request.user.id
        company = Company.objects.filter(owner__id=owner_id).first()
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('/mycompany/')
        return render(request, 'vacancy/company.html', context={'form': form, 'company_name': company.name})


class MyVacancyCreateView(LoginRequiredMixin, CreateView):
    def get(self, request, *args):
        return render(request, 'vacancy/myvacancy-create.html', context={'form': VacancyForm})

    def post(self, request, *args):
        form = VacancyForm(request.POST)
        company = get_object_or_404(Company, owner_id=request.user.id)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = company
            vacancy.save()
            return redirect('/mycompany/vacancies/')
        return render(request, 'vacancy/myvacancy-create.html', context={'form': form})


class MyVacancyListView(ListView):

    def get(self, request, *args):
        owner_id = request.user.id
        company = get_object_or_404(Company, owner_id=owner_id)
        vacancies = Vacancy.objects.filter(company=company)
        if vacancies.count() == 0:
            return render(request, 'vacancy/myvacancies-empty.html')
        return render(request, 'vacancy/myvacancies.html', context={'vacancies': vacancies})


class MyVacancyDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs['vacancy_id'])
        form = VacancyForm(instance=vacancy)
        return render(request, 'vacancy/myvacancy.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs['vacancy_id'])
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('/mycompany/vacancies/')
        return render(request, 'vacancy/myvacancy.html', context={'form': form})


class MySignupView(CreateView):
    # form_class = UserCreationForm
    form_class = MySignUpForm
    success_url = '/login/'
    template_name = 'vacancy/signup.html'

    def post(self, request, *args):
        User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password1'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
        )
        return redirect('/login/')


class MyLoginView(LoginView):
    success_url = '/'   # This parameter seems doesn't work. Instead, I'm using settings.LOGIN_REDIRECT_URL = '/'.
    template_name = 'vacancy/login.html'


