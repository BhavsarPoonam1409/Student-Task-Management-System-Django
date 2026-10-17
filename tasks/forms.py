from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = [
            'title',
            'description',
            'priority',
            'due_date',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter your task title'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your task',
                'rows': 4
            }),

            'due_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})