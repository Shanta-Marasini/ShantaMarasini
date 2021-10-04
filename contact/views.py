from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.urls import reverse_lazy

# Create your views here.
def contactme(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            new_contact = contact_form.save(commit=False)
            new_contact.save()
            contact_form = ContactForm()

    else:
        contact_form = ContactForm()

    return render(request, 'contact/contact.html', {'contact_form': contact_form})