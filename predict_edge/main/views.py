from typing import Any
from django.views.generic import TemplateView
from .models import Clothing, Clothes_Sizes, Clothes_Colors, ClothingImage

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
        pk = self.kwargs.get('pk')
        
        clothing = Clothing.objects.get(id=pk)
        context['clothing'] = clothing
        
        images = ClothingImage.objects.filter(clothing=clothing)
        context['images'] = images
        
        colors = Clothes_Colors.objects.filter(clothing=clothing)
        context['colors'] = colors
        
        sizes = Clothes_Sizes.objects.filter(clothing=clothing)
        context['sizes'] = sizes
        
        clothes = Clothing.objects.all()
        context['clothes'] = clothes
        
        return context