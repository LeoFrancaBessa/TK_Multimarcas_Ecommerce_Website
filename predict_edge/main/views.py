from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        clothes = Clothing.objects.all()
        context['clothes'] = clothes
        return context


class ClothingDetailsView(TemplateView):
    template_name = 'main/clothing-detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        clothing = Clothing.objects.get(id=1)
        context['clothing'] = clothing
        images = ClothingImage.objects.filter(clothing=clothing)
        context['images'] = images
        colors = Clothes_Colors.objects.filter(clothing=clothing)
        context['colors'] = colors
        sizes = Clothes_Sizes.objects.filter(clothing=clothing)
        context['sizes'] = sizes
        return context