from django import forms
from django.forms import ModelForm
from ..models import Role

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']
