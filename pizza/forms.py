from django import forms
from .models import PizzaVault

class PizzaForm(forms.ModelForm):
	class Meta:
		model = PizzaVault
		fields = '__all__'

