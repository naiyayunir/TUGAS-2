from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_item_catalog = CatalogItem.objects.all()
    context = {
        'list_item' : data_item_catalog,
        'nama' : 'Naiya Dwita Ayunir',
        'npm' : '2106651976'
    }
    return render(request, "katalog.html", context)
