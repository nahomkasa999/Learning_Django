from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import ItemForm
from .models import Item

# Create your views here.
#CRUd
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'inventory/create_item.html', {'form':form})


def update_item(request, item_id):
    item = Item.objects.get(item_id=item_id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'inventory/update_item.html', {'form':form})

def delete_item(request, item_id):
    item = Item.objects.get(item_id=item_id)
    item.delete()
    return redirect('home')

def view_item(request, item_id):
    item = Item.objects.get(item_id=item_id)
    return render(request, 'inventory/view_item.html', {'item':item})

#Home View
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})