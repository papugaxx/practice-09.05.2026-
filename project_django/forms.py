from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'notes']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': "Введіть ім'я"
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': "Введіть прізвище"
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': "example@gmail.com"
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': "+380..."
            }),
            'notes': forms.Textarea(attrs={
                'placeholder': "Додаткові примітки",
                'rows': 4
            }),
        }