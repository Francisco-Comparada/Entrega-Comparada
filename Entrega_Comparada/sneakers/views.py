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


def Shop_single_Jordans(request, pk):
    if request.method == 'GET':
        jordans = Jordans.objects.get(pk=pk)
        context = {'jordans':jordans}
        return render(request, 'jordans/Shop_single_Jordans.html', context=context)
        #para cuando use el boton buy o add to cart
    elif request.method == 'POST':
        jordans = Jordans.objects.get(pk=pk)
        return redirect('Jordans/list_Jordans.html')




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

def Shop_single_Air_Force(request, pk):
    if request.method == 'GET':
        air_forces = Air_Force.objects.get(pk=pk)
        context = {'air_forces':air_forces}
        return render(request, 'Air_Force/Shop_single_Air_Force.html', context=context)
        #para cuando use el boton buy o add to cart
    elif request.method == 'POST':
        air_forces = Air_Force.objects.get(pk=pk)
        return redirect('Air_Force/list_air_forces.html')

    

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

def Shop_single_Accessories(request, pk):
    if request.method == 'GET':
        Accessorie = Accessories.objects.get(pk=pk)
        context = {'Accessorie':Accessorie}
        return render(request, 'Accessories/Shop_single_Accessories.html', context=context)
        #para cuando use el boton buy o add to cart
    elif request.method == 'POST':
        Accessorie = Accessories.objects.get(pk=pk)
        return redirect('Accessories/list_Accessories.html')

#Search Jordans Air Force Accessories 

def search_products(request):
    search = request.GET['search']
    sneakers_jordans =Jordans.objects.filter(model__icontains=search)
    sneakers_air_forces = Air_Force.objects.filter(model__icontains=search)
    Accessories_ = Accessories.objects.filter(name__icontains=search)
    context = {
        'sneakers_jordans': sneakers_jordans,
        'sneakers_air_forces': sneakers_air_forces,
        'Accessories_':Accessories_
    }
    return render(request, 'search_products.html', context=context)