from django.shortcuts import render
from .forms import ApplicationForm
from .models import Application
from django.contrib import messages
from django.core.mail import EmailMessage



def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date =form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            Application.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )

            messages_body=f"Hello {first_name}, Your application has been submitted successfully!"
            email_message=EmailMessage("Application Form confirmation!", messages_body, to=[email])
            email_message.send()

            messages.success(request,"From submitted successfully!")
    return render(request, 'index.html')

