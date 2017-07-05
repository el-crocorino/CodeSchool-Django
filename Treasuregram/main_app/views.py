from django.shortcuts import render

# Create your views here.

def index(request):
    name    = 'Gold Nugget'
    value   = 1000.00
        
    return render(request, 'index.html', {'treasures': treasures}) 

class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url
        
treasures = [
    Treasure('Gold Nugget', 500.0, 'gold', "Curly's Creek, NM", 'https://vignette3.wikia.nocookie.net/clubpenguin/images/c/cf/Gold_Nugget.png/revision/latest?cb=20131116003237'),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Fall, CO", 'http://www.pyritexpertise.com/images/pyrite.png'),
    Treasure('Coffee Can', 20.0, 'tin', "ACME, CA", 'https://cdn0.rubylane.com/shops/drury/9894-2.1L.jpg'),
]