from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')
def register(request):
    form=UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'User has been registered.')
    return render(request, 'reg/register.html', {'form':form })