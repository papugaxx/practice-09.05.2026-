from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Contact
from .forms import ContactForm


def contact_list(request):
    search = request.GET.get('search', '')

    contacts = Contact.objects.all()

    if search:
        contacts = Contact.objects.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search)
        )

    return render(request, 'project_django/contact_list.html', {
        'contacts': contacts,
        'search': search
    })


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(request, 'project_django/add_contact.html', {
        'form': form
    })