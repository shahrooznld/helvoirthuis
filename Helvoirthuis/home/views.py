from django.shortcuts import render

from .forms import Registrationform
from .models import posts
from .models import menutab
from django.contrib import messages

def home(request, ):

    template = "content/homepage.html"
    qs = posts.objects.all()
    ms = menutab.objects.all()


    context = {
        'object_list': qs,
        'menu_list': ms,
        'menuactive': 'Home'
    }
    return render(request, template, context)


def contact(request):
    ms = menutab.objects.all()
    if request.method == 'POST':

        form = Registrationform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name, email)
            messages.info(request, 'Your password has been changed successfully!')
            form.save()
    template = "content/contactus.html"
    context = {
        'form': Registrationform,
        'menu_list': ms,
        'menuactive': 'Contact Us'
    }
    return render(request, template, context)
