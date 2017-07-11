from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm

# Create your views here.

def index(request):
    name    = 'Gold Nugget'
    value   = 1000.00
    treasures = Treasure.objects.all
    form = TreasureForm()
    return render(request, 'index.html', {'treasures': treasures, 'form': form}) 

def detail(request, treasure_id):
    treasure = Treasure.objects.get( id = treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})
 
def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/')

