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
