from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .utils import get_clothing_data

class IndexView(TemplateView):
    login_url = "login"
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        clothes = list(range(5))
        context['clothes'] = clothes
        return context