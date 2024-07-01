from django.contrib import admin
from .models import UserProfile, Brand, Category, Material, Type, SubType, Clothing, ClothingImage, Clothes_Sizes, Clothes_Colors

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'date_of_birth', 'gender', 'state', 'city', 'neighborhood', 'address', 'address_number']
    # Adicione outros campos conforme necessário

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    # Adicione outros campos conforme necessário

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    # Adicione outros campos conforme necessário

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    # Adicione outros campos conforme necessário

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    # Adicione outros campos conforme necessário

@admin.register(SubType)
class SubTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    # Adicione outros campos conforme necessário

class ClothingImageInline(admin.TabularInline):
    model = ClothingImage

class ClothesSizesInline(admin.TabularInline):
    model = Clothes_Sizes

class ClothesColorsInline(admin.TabularInline):
    model = Clothes_Colors

@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'gender', 'brand', 'category', 'material', 'type', 'subtype', 'created_at', 'updated_at']
    inlines = [ClothingImageInline, ClothesSizesInline, ClothesColorsInline]
    # Adicione outros campos conforme necessário

@admin.register(ClothingImage)
class ClothingImageAdmin(admin.ModelAdmin):
    list_display = ['clothing', 'image', 'principal']
    # Adicione outros campos conforme necessário

@admin.register(Clothes_Sizes)
class ClothesSizesAdmin(admin.ModelAdmin):
    list_display = ['clothing', 'size', 'count']
    # Adicione outros campos conforme necessário

@admin.register(Clothes_Colors)
class ClothesColorsAdmin(admin.ModelAdmin):
    list_display = ['clothing', 'color', 'count']
    # Adicione outros campos conforme necessário
