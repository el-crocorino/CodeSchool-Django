from django.shortcuts import render

# Create your views here.

def index(request):
    name    = 'Gold Nugget'
    value   = 1000.00
        
    return render(request, 'index.html', {'treasures': treasures}) 

class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        
treasures = [
    Treasure('Gold Nugget', 500.0, 'gold', "Curly's Creek, NM"),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Fall, CO"),
    Treasure('Coffee Can', 20.0, 'tin', "ACME, CA"),
]