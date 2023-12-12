from store.models import Product


class Cart():
    def __init__(self, request) -> None:
        # Get the current session from the request
        self.session = request.session

        # Get the existing cart from the session using the key 'session_key'
        cart = self.session.get("session_key")

        # If the user is new (no session_key in the session), create a new session and cart
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure that 'cart' is available on all pages
        self.cart = cart
    
    def add(self,product):
        product_id = str(product.id)
        
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
            
        self.session.modified = True
    
    def __len__(self):
        
        return len(self.cart)
    
    
    def get_prods(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        
        return products