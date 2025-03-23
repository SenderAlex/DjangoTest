from .models import Goat
from django.forms import ModelForm, TextInput, NumberInput, Textarea


class GoatForm(ModelForm):
    class Meta:
        model = Goat
        fields = '__all__'  # ['first_name', 'last_name', 'scores', 'clubs']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'scores': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество голов'}),
            'clubs': Textarea(attrs={'class': 'form-control', 'placeholder': 'Клубы'})
        }