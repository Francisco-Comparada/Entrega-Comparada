from django import forms

class Formulario_Jordans (forms.Form):
    model=forms.CharField(max_length=40)
    price=forms.IntegerField()
    coulor=forms.CharField(max_length=40)
    description=forms.CharField(max_length=400)
    stock=forms.IntegerField()
    img= forms.ImageField()
    
class Formulario_Air_Force (forms.Form):
    model=forms.CharField(max_length=40)
    price=forms.IntegerField()
    coulor=forms.CharField(max_length=40)
    description=forms.CharField(max_length=400)
    stock=forms.IntegerField()
    img= forms.ImageField()
 
class Formulario_Accessories(forms.Form):
    name=forms.CharField(max_length=40)
    price=forms.IntegerField()
    description=forms.CharField(max_length=400)
    stock=forms.IntegerField()
    img= forms.ImageField()