from django import forms
from .models import Producer,Production

class ProducerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Producer
        fields=['name','email','password','nationality','contact','production_house','production_house_add','local_agent','local_agent_add','passport_no','passport_validity']
        widgets = {
            'passport_validity': DateInput(),
        }

class ProductionForm(forms.ModelForm):
	class Meta:
		model=Production
		fields=['film','director','cinematographer','art_director','script','shoot_timing','shoot_start','shoot_end','location']
		widgets = {
		    'shoot_start': DateInput(),
		    'shoot_end':DateInput(),
		    'shoot_timing':TimeInput(),
		}
