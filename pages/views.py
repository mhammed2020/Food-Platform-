from django.shortcuts import render

# Create your views here.
from products.models import Product
def home(request) :

    products = Product.objects.all()

    context = {
        'products' : products
    }

    return render(request,'pages/home.html',context)

def about(request) :
    
    return render(request,'pages/about.html')


def restaurant(request) :
    
    return render(request,'pages/restaurant.html')