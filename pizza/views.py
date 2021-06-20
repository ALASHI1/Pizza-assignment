from django.shortcuts import render,get_object_or_404
from .models import *
from .forms import PizzaForm
# Create your views here.

def home(request):
	if request.method == 'POST':
		form = PizzaForm(request.POST)
		if form.is_valid():
			pizza = form.save()
			return render(request,'orderpage.html',{'pizza':pizza})
	else:
		form = PizzaForm()
	
	return render(request,'index.html',{'form':form})


def edit(request,id):
	pizza = get_object_or_404(PizzaVault,id=id)
	if request.method == "POST":
		form = PizzaForm(request.POST, instance=pizza)
		if form.is_valid():
			pizza = form.save()
			pizza.save()
			return render(request,'orderpage.html',{}) 
	else:
		form = PizzaForm(instance=pizza)
	return render(request, 'edit.html', {'form': form})