from django import forms
from .models import *


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


class KafedraForm(forms.ModelForm):
    class Meta:
        model = Kafedra
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "subject": forms.Select(attrs={'class': 'form-control'}),
            "kafedra_id": forms.Select(attrs={'class': 'form_control'})
        }



class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "kafedra_id": forms.Select(attrs={'class': 'form-control'}),
            "mentor_id": forms.Select(attrs={'class': 'form-control'}),
        }



class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "phone_number": forms.NumberInput(attrs={'class': 'form-control'}),
            "date_of_birth": forms.DateInput(attrs={'class': 'form-control'}),
            "group_id": forms.Select(attrs={'class': 'form-control'}),
        }


































