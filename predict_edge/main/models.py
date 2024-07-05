from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(null=True, blank=True,max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=2, choices=[
                                                    ("M", "MASCULINO"),
                                                    ("F", "FEMININO"),
                                                ])
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address_number = models.CharField(max_length=200)


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")

    class Meta:
        ordering = ["name"]
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")

    class Meta:
        ordering = ["name"]
        verbose_name = "Material"
        verbose_name_plural = "Materiais"

    def __str__(self) -> str:
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=100, verbose_name="Atributo")

    class Meta:
        verbose_name = "Atributo"
        verbose_name_plural = "Atributos"

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="values", verbose_name="Atributo")
    value = models.CharField(max_length=100, verbose_name="Valor")

    class Meta:
        verbose_name = "Valor do Atributo"
        verbose_name_plural = "Valores do Atributo"

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"


class Clothing(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    gender = models.CharField(max_length=20, choices=[('Masculino', 'Masculino'), 
                                                         ('Feminino', 'Feminino')], verbose_name="Gênero")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name="Marca")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Categoria")
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, verbose_name="Material")
    attributes = models.ManyToManyField(AttributeValue, blank=True, verbose_name='Atributos')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado Em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado Em")

    class Meta:
        ordering = ["updated_at"]
        verbose_name = "Roupa"
        verbose_name_plural = "Roupas"

    def __str__(self) -> str:
        return self.name


class ClothingImage(models.Model):
    clothing = models.ForeignKey(Clothing, related_name='images', on_delete=models.CASCADE)
    principal = models.BooleanField(default=False, verbose_name="Imagem Principal?")
    image = models.ImageField(upload_to='media/', verbose_name="Imagem")

    class Meta:
        verbose_name = "Imagem Roupa"
        verbose_name_plural = "Imagens Roupa"


class Clothes_Sizes(models.Model):
    clothing = models.ForeignKey(Clothing, related_name='sizes', on_delete=models.CASCADE)
    size_choices = [
        ('PP', 'PP'),
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
    ]
    size = models.CharField(max_length=4, choices=size_choices, verbose_name="Tamanho")
    count = models.IntegerField()

    class Meta:
        verbose_name = "Tamanho Roupa"
        verbose_name_plural = "Tamanhos Roupa"


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
        ('#FFFFF0', 'bege'),
        ('#40E0D0', 'turquesa'),
        ('#FF4500', 'laranja escuro'),
        ('#FF6347', 'salmão'),
        ('#FFE4B5', 'mocassim'),
        ('#BDB76B', 'caqui'),
        ('#008080', 'teal'),
        ('#FA8072', 'salmon claro'),
        ('#DC143C', 'carmesim'),
        ('#7FFFD4', 'aquamarine'),
        ('#F0E68C', 'khaki claro'),
        ('#B8860B', 'ouro escuro'),
        ('#00CED1', 'azul-celeste'),
        ('#6495ED', 'azul ardósia'),
        ('#CD5C5C', 'marrom rosado'),
        ('#556B2F', 'verde oliva escuro'),
        ('#4B0082', 'índigo'),
        ('#2F4F4F', 'cinza ardósia escuro')
    ]
    color = ColorField(choices=COLOR_PALETTE, verbose_name="Cor")
    count = models.IntegerField()

    class Meta:
        verbose_name = "Cor Roupa"
        verbose_name_plural = "Cores Roupa"


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cartItems', on_delete=models.CASCADE)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)
    color = models.ForeignKey(Clothes_Colors, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(Clothes_Sizes, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Item de Carrinho"
        verbose_name_plural = "Itens de Carrinho"


class Favorites(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="favorites",  on_delete=models.CASCADE)
    clothing = models.ForeignKey(Clothing,  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Favoritos"
        verbose_name_plural = "Favoritos"