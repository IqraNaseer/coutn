from django import forms 
from .models import select
  
class selectForm(forms.ModelForm): 
  
    class Meta: 
        model = select 
        fields = ['image'] 