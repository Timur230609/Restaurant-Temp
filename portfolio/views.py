from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            new_contact = Contact(name=name, email=email, content=content)
            new_contact.save()
            messages.success(request, "Your message was successfully sent!")
            return redirect('home-page')  # Bu yerda HttpResponseRedirect o'rniga redirect() ishlatilmoqda
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('contact')
    
    return render(request, 'contact.html')



def index_view(request):
 return render(request,'index.html')


def services_view(request):
 return render(request,'service.html')

def about_view(request):
 return render(request,'about.html')

def testimonial_view(request):
 return render(request,'testimonial.html')

def works_view(request):
 return render(request,'works.html')
