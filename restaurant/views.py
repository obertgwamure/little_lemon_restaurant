from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from .models import Menu


def home(request):
    return render(request, 'restaurant/index.html')

def about(request):
    return render(request, 'restaurant/about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'restaurant/book.html', context)

def menu(request):
    menu_items = Menu.objects.all().order_by('name')
    context = {
        'menu' : menu_items
    }
    return render(request, 'restaurant/menu.html', context)

def menu_item(request, pk):
    menu_item = Menu.get_object_or_404(pk=pk)
    context = {
        'menu_item': menu_item,
    }
    return render(request, 'restaurant/menu-item.html', context)