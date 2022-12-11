from django.shortcuts import render, HttpResponse, redirect
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='log_url')
def addOrder(request):
    form = OrderForm()
    template_name = 'app1/add.html'
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='log_url')
def showOrder(request):
    data = Order.objects.all()
    template_name = 'app1/show.html'
    context = {'data': data}
    return render(request, template_name, context)

def updateOrder(request, pk):
    obj = Order.objects.get(id=pk)
    form = OrderForm(instance=obj)
    template_name = 'app1/add.html'
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def deleteOrder(request, pk):
    obj = Order.objects.get(id = pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'app1/confirm.html'
    context = {'data': obj}
    return render(request, template_name, context)


    
    
    
    