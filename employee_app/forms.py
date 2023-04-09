from django.forms import ModelForm
from .models import Employee


class AddEmpFrom(ModelForm):
    class Meta:
        model = Employee
        fields = ["first_name", "last_name", "dept", "role", "salary", "bonus", "phone_number"]