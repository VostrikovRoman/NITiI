from .models import Students
from django.forms import ModelForm, TextInput, DateInput, Select, CheckboxInput, FileInput

class StudentsForm(ModelForm):
    class Meta():
        model = Students
        fields = ['surname', 'name', 'lastname', 'birthday', 'group', 'gender', 'is_leader', 'photo']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'id': 'surname'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'id': 'name'
            }),
            "lastname": TextInput(attrs={
                'class': 'form-control',
                'id': 'lastname'
            }),
            "photo": FileInput(attrs={
                'class': 'form-control',
                'id': 'photo',
                'accept': 'image/*'
            }),
            "gender": Select(attrs={
                'class': 'form-control',
                'id': 'gender'
            }),
            "birthday": DateInput(attrs={
                'class': 'form-control',
                'id': 'birthday'
            }),
            "group": Select(attrs={
                'class': 'form-control',
                'id': 'group'
            }),
            "is_leader": CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'is_leader'
            })
        }