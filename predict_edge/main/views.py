from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class IndexView(TemplateView):
    login_url = "login"
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        clothes = Clothing.objects.all()
        images = ClothingImage.objects.all()
        context['clothes'] = clothes
        context['clothing_images'] = images
        return context