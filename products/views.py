from django.shortcuts import render

# Create your views here.


def product_list(request):


    return render (request,'products/product_list.html')


def product(request,id):
    

    return render (request,'products/product.html')