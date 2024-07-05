from django.contrib import admin
from .models import UserProfile, Brand, Category, Material, Attribute, AttributeValue, Clothing, ClothingImage, Clothes_Sizes, Clothes_Colors
from django import forms

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


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInline]


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ['attribute', 'value']


class ClothingImageInline(admin.TabularInline):
    model = ClothingImage


class ClothesSizesInline(admin.TabularInline):
    model = Clothes_Sizes


class ClothesColorsInline(admin.TabularInline):
    model = Clothes_Colors


class ClothingForm(forms.ModelForm):
    attributes = forms.ModelMultipleChoiceField(
        queryset=AttributeValue.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple("Attributes", is_stacked=False),
        required=False
    )

    class Meta:
        model = Clothing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['attributes'].initial = self.instance.attributes.all()

    def save(self, commit=True):
        clothing = super().save(commit=False)
        if commit:
            clothing.save()
        if clothing.pk:
            clothing.attributes.set(self.cleaned_data['attributes'])
            self.save_m2m()
        return clothing


@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    form = ClothingForm
    list_display = ['name', 'brand', 'category', 'price', 'gender']
    search_fields = ['name', 'description']
    list_filter = ['gender', 'brand', 'category', 'material']
    inlines = [ClothingImageInline, ClothesSizesInline, ClothesColorsInline]

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'gender', 'brand', 'category', 'material')
        }),
        ('Attributes', {
            'fields': ('attributes',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ['created_at', 'updated_at']


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
