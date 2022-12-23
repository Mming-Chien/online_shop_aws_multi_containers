from .cart import Cart 
def cart(request):
	''' request context processor for cart '''
	return {'cart':Cart(request)}