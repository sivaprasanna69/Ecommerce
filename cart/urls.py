from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'cart'
urlpatterns = [

	path('', views.view, name='view'),

	path('<slug:slug>/',views.update_cart, name='update_cart'),

]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)