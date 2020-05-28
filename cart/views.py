from django.shortcuts import render

# Create your views here.

from .models import Cart



def view(request):

	cart = Cart.objects.all()[0]
	template = 'cart/view.html'
	context = {'cart': cart}
	return render(request, template, context)
