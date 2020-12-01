from django.shortcuts import render,get_object_or_404

# Create your views here.

from . models import Product

def product_list(request):
     

    products = Product.objects.all()

    context = {
        'products' : products
    }



    return render (request,'products/product_list.html',context)


def product(request,id):

    product = get_object_or_404(Product,id=id)

    
    context = {
        'product' : product
    }



    return render (request,'products/product.html',context)



def search(request):
    

    return render (request,'products/search.html')