from .models import Groups
from django.forms import ModelForm, TextInput, Select, NumberInput

class GroupsForm(ModelForm):
    class Meta():
        model = Groups
        fields = ['name', 'course', 'speciality', 'count_of_students']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'id': 'name'
            }),
            "course": NumberInput(attrs={
                'class': 'form-control',
                'id': 'course'
            }),
            "speciality": Select(attrs={
                'class': 'form-control',
                'id': 'speciality'
            }),
            "count_of_students": NumberInput(attrs={
                'class': 'form-control',
                'id': 'count_of_students'
            })
        }