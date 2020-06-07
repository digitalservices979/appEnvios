from django.urls import path

from . import views

urlpatterns = [
	path('listaMascarilla/',views.MascarillaList.as_view()),
	path('createPedido/',views.PedidoCreate.as_view())
]