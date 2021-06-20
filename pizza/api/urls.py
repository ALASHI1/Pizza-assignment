from django.urls import path
from . import views

app_name = 'pizza'

urlpatterns = [
	path('list/',views.PizzaVaultList.as_view(), name='list'),
	path('detail/<int:pk>',views.PizzaVaultDetail.as_view(), name='detail'),
	path('create/',views.PizzaVaultCreate.as_view(), name='create'),

]
