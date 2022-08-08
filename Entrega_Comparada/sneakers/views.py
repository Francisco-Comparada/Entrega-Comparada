from django.shortcuts import render, redirect
from sneakers.forms import Formulario_Air_Force, Formulario_Jordans
from sneakers.models import Jordans, Air_Force


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
                year=form.cleaned_data['year'],
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
                year=form.cleaned_data['year'],
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
   # sneakers_air_force = Air_Force.objects.filter(model__icontains=search)
    sneakers_jordans = Jordans.objects.filter(model__icontains=search)
   # context = {'sneakers_air_force':sneakers_air_force}
    context = {' sneakers_jordans': sneakers_jordans}
    return render(request, 'Sneaker/search_products.html', context=context)