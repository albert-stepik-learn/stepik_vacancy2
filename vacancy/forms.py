from django import forms

from stepik_vacancy2.settings import MEDIA_COMPANY_IMAGE_DIR
from vacancy.models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'location', 'logo', 'description', 'employee_count']
