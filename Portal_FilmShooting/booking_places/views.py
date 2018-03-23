from django.shortcuts import render
from .forms import ApplicationForm

# Create your views here.
def home(request):
    render(request,'base.html',{})

def application_form(request):
    if request.method == 'POST':
        application_form = ApplicationForm(request.POST or None)
        if application_form.is_valid():

            if 'script' in request.FILES and 'undertaking' in request.FILES:
                application_form.script = request.FILES['script']
                application_form.undertaking = request.FILES['undertaking']
                # Now we save the application form
                application_form.save()

            return render(request,'base.html',{}) # change to redirect 
    else:
        application_form = ApplicationForm()
    return render(request,'application_form.html',{'application_form':application_form})
