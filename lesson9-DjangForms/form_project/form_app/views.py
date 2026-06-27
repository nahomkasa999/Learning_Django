from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def home_view(request):
    return render(request, 'form_app/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            return redirect('contact_success')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'form_app/contact.html', context)


def contact_success_view(request):
    return render(request, 'form_app/contact_success.html')