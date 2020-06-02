from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from products.models import product

from .models import Cart, CartItem



def view(request):
	try:
		the_id = request.session['cart_id']
		print("inside try")
		print(the_id)
	except:
		the_id = None
		print("inside except")
		print(the_id)
	if the_id:
		cart = Cart.objects.get(id=the_id)
		context = {"cart": cart}
	else:
		print("hello")
		empty_message = "your cart is empty"
		context = {"empty": True, "empty_message": empty_message}


	template = 'cart/view.html'
	return render(request, template, context)

def update_cart(request, slug, qty):

	try:

		the_id = request.session['cart_id']
	except:

		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id

	cart = Cart.objects.get(id=the_id)

	try:

		prd = product.objects.get(slug=slug)
	except product.DoesNotExists:

		pass
	except:

		pass

	cart_item, created = CartItem.objects.get_or_create(cart=cart,product=prd)
	if created:
		print ("yeah")
	if qty == 0:
		cart_item.delete()
	else:
		cart_item.quantity = qty
		cart_item.save()

	#if cart_item in cart.products.all():
		#cart.items.remove(cart_item)
		
	#else:
		#cart.items.add(cart_item)

	new_total = 0.00
	for item in cart.cartitem_set.all():
		line_total = float(item.product.price) * item.quantity
		new_total += line_total
	cart.total = new_total
	cart.save()
	request.session['items_total'] = cart.cartitem_set.count()
	print("hello")
	return HttpResponseRedirect('/cart')




