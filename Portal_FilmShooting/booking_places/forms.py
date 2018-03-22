from django import forms
from .models import Producer,Production

class ProducerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Producer
        fields=['name','email','password','nationality','contact','production_house','production_house_add','local_agent','local_agent_add','passport_no','passport_validity']
        widgets = {
            'passport_validity': forms.DateInput(),
        }

class ApplicationForm(forms.ModelForm):
	"""Application Form"""
	class Meta:
		model=Production
		fields=['producer','production_house','production_house_add','contact','local_line_producer','local_line_producer_add','film','director','cinematographer','art_director','script','shoot_timing','shoot_start','shoot_end','location']
		widgets = {
		    'shoot_start': forms.DateInput(),
		    'shoot_end':forms.DateInput(),
		    'shoot_timing':forms.TimeInput(),
		}
		
		
			