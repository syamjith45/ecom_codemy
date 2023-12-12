from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_products = cart.get_prods
    return render(request,"cart_summary.html",{'cart_products':cart_products})
def cart_add(request):
    #get the cart
    cart= Cart(request)
    if request.POST.get('action')=='post':
         
        product_id = int(request.POST.get('product_id'))
        # lookup product in DB
        product= get_object_or_404(Product,id=product_id)
        
        cart.add(product=product)
        #get quantity
        cart_quantity=cart.__len__()
        # response=JsonResponse({'Product Name: ': product.p_name})
        response=JsonResponse({'qty': cart_quantity})
        return response
        
    
    return render(request,"cart_summary.html")
def cart_delete(request):
    return render(request,"cart_summary.html")
def cart_update(request):
    return render(request,"cart_summary.html")
