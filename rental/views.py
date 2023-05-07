from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomerRegistrationForm
from .models import Customer

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer.objects.create(
                user=user,
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                address=form.cleaned_data.get('address'),
                phone=form.cleaned_data.get('phone')
            )
            login(request, user)
            return redirect('home')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def home(request):
    return render(request, 'home.html')
    