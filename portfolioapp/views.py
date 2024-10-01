from django.shortcuts import render,redirect
from django.http import HttpResponse
from . send_email import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_subject = f'Message from {name}: {subject}'

            send_mail(
                subject = full_subject,
                message=message, 
                from_email = settings.DEFAULT_FROM_EMAIL,
                recipient_list = [settings.DEFAULT_FROM_EMAIL],
                fail_silently = False,
            )
            return redirect('success.html')
    else:
        form=ContactForm
    return render(request, 'index.html', {'form':form}) 

def success_view(request):
    return render(request, 'success.html')                  
