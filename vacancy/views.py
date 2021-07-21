from django.db.models import Count
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Company,  Speciality, Vacancy


def main_view(request):
    return render(
        request,
        'vacancy/index.html',
        context={
            'specialities': Speciality.objects.annotate(vacancy_count=Count('vacancies')),
            'companies': Company.objects.annotate(vacancy_count=Count('vacancies')),
        },
    )


class VacancyListView(ListView):
    model = Vacancy


class VacancyDetailView(DetailView):
    model = Vacancy


class SpecialityDetailView(DetailView):
    model = Speciality
    slug_field = 'code'
    slug_url_kwarg = 'code'

    def get_context_data(self, **kwargs):
        context = super(SpecialityDetailView, self).get_context_data(**kwargs)
        context['vacancy_list'] = Vacancy.objects.filter(speciality_id=self.object.pk)
        return context


class CompanyListView(ListView):
    model = Company


class CompanyDetailView(DetailView):
    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['vacancy_list'] = Vacancy.objects.filter(company__id=self.object.pk)
        return context
