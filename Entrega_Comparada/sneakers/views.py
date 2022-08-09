from re import search
from unicodedata import name
from django.shortcuts import render, redirect
from sneakers.forms import Formulario_Air_Force, Formulario_Jordans, Formulario_Accessories
from sneakers.models import Jordans, Air_Force,Accessories


#Jordans
def add_Jordans(request):  
    if request.method == 'POST':
        form = Formulario_Jordans(request.POST,request.FILES)
        if form.is_valid():
            add_Jordans = Jordans.objects.create (
                model=form.cleaned_data['model'],
                price=form.cleaned_data['price'],
                coulor=form.cleaned_data['coulor'],
                description=form.cleaned_data['description'],
                stock = form.cleaned_data['stock'],
                img = form.cleaned_data['img'],
            )
            return redirect(list_Jordans)
            
    elif request.method == 'GET':
        form = Formulario_Jordans()
        context = {'form':form}
        return render(request, 'Jordans/add_Jordans.html', context=context)


def list_Jordans(request):
    jordans = Jordans.objects.all()
    print(len(jordans))
    context = {
        'jordans':jordans
    }
    return render(request, 'Jordans/list_Jordans.html', context=context)
#Jordans


#Air_force
def add_Air_Force(request):  
    if request.method == 'POST':
        form = Formulario_Air_Force(request.POST,request.FILES)
        if form.is_valid():
            add_Air_force = Air_Force.objects.create (
                model=form.cleaned_data['model'],
                price=form.cleaned_data['price'],
                coulor=form.cleaned_data['coulor'],
                description=form.cleaned_data['description'],
                stock = form.cleaned_data['stock'],
                img = form.cleaned_data['img'],
            )
            return redirect(list_Air_Force)
            
    elif request.method == 'GET':
        form = Formulario_Air_Force()
        context = {'form':form}
        return render(request, 'Air_Force/add_Air_Force.html', context=context)


def list_Air_Force(request):
    air_forces = Air_Force.objects.all()
    print(len(air_forces))
    context = {
        'air_forces':air_forces
    }
    return render(request, 'Air_Force/list_Air_Force.html', context=context)




def search_products(request):
    search = request.GET['search']
    sneakers_jordans =Jordans.objects.filter(model__icontains=search)
    context = {'sneakers_jordans': sneakers_jordans}
    return render(request, 'search_products.html', context=context)
    
def search_products_Air_Force(request):
    search = request.GET['search']
    sneakers_air_forces = Air_Force.objects.filter(model__icontains=search)
    context = {'sneakers_air_forces': sneakers_air_forces}
    return render(request, 'search_products_Air_Force.html', context=context) 


# Accessories
def add_Accessories(request):  
    if request.method == 'POST':
        form = Formulario_Accessories(request.POST,request.FILES)
        if form.is_valid():
            add_Accessories = Accessories.objects.create (
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                description=form.cleaned_data['description'],
                stock = form.cleaned_data['stock'],
                img = form.cleaned_data['img'],
            )
            return redirect(list_Accessories)
            
    elif request.method == 'GET':
        form = Formulario_Accessories()
        context = {'form':form}
        return render(request, 'Accessories/add_Accessories.html', context=context)


def list_Accessories(request):
    Accessories_ = Accessories.objects.all()
    print(len(Accessories_))
    context = {
        'Accessories_':Accessories_
    }
    return render(request, 'Accessories/list_Accessories.html', context=context)