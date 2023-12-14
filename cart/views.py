from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_products = cart.get_prods
    quantities= cart.get_quants
    return render(request,"cart_summary.html",{'cart_products':cart_products,"quantities":quantities})
def cart_add(request):
    #get the cart
    cart= Cart(request)
    if request.POST.get('action')=='post':
         #get stuffs
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # lookup product in DB
        product= get_object_or_404(Product,id=product_id)
        #save to session
        cart.add(product=product,quantity=product_qty)
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
