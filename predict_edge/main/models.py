from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=2, choices=[
                                                    ("M", "MASCULINO"),
                                                    ("F", "FEMININO"),
                                                ])
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address_number = models.CharField(max_length=200)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class SubType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Clothing(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=1, choices=[('M', 'Masculino'), 
                                                         ('F', 'Feminino')])
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    subtype = models.ForeignKey(SubType, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ClothingImage(models.Model):
    clothing = models.ForeignKey(Clothing, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='clothing_images/')


class Clothes_Sizes(models.Model):
    clothing = models.ForeignKey(Clothing, related_name='sizes', on_delete=models.CASCADE)
    size_choices = [
        ('PP', 'PP'),
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
    ]
    size = models.CharField(max_length=4, choices=size_choices)
    count = models.IntegerField()


class Clothes_Colors(models.Model):
    clothing = models.ForeignKey(Clothing, related_name='colors', on_delete=models.CASCADE)
    COLOR_PALETTE = [
        ('#FFFFFF', 'branco'),
        ('#000000', 'preto'),
        ('#808080', 'cinza'),
        ('#FF0000', 'vermelho'),
        ('#FFA500', 'laranja'),
        ('#FFFF00', 'amarelo'),
        ('#008000', 'verde'),
        ('#0000FF', 'azul'),
        ('#800080', 'roxo'),
        ('#FFC0CB', 'rosa'),
        ('#800000', 'marrom'),
        ('#00FFFF', 'ciano'),
        ('#A52A2A', 'castanho'),
        ('#FFD700', 'dourado'),
        ('#000080', 'azul-marinho'),
        ('#8B0000', 'vermelho escuro'),
        ('#800080', 'roxo'),
        ('#00FF00', 'verde-limão'),
        ('#FF00FF', 'magenta'),
        ('#FFFFF0', 'bege')
    ]
    color = color = ColorField(choices=COLOR_PALETTE)
    count = models.IntegerField()
