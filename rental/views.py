from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup_Customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST or None)

        if form.is_valid():
            form.save()

        return render(request,'signup_Customer.html',{'msg':'Customer Signup'})
    else:
        return render(request,'signup_Customer.html',{'msg':'Customer Signup'})
    
def entries(request):
    return render(request, 'entries.html', {'entries':Customer.objects.all()})