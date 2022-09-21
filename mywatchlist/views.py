from django.shortcuts import render
from mywatchlist.models import Watchlist_models
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_movie_mywatchlist = Watchlist_models.objects.all()
    context = {
        'list_movie' : data_movie_mywatchlist,
        'nama' : 'Naiya Dwita Ayunir',
        'npm' : '2106651976'
    }
    return render(request, "mywatchlist.html", context)
    
def show_xml(request):
    data = Watchlist_models.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Watchlist_models.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = Watchlist_models.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")                                                                                                                                                                                                                                                                                                                                                                                                                                                             