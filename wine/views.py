from django.http import JsonResponse
from wine import models
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def wine_list(request):
    wines = models.Wine.objects.all()
    dumped_wines = []
    for wine in wines:
        dumped_wines.append({
            "category": wine.get_category_display(),
            "title": wine.title,
            "sort_of_grape": wine.sort_of_grape,
            "price": wine.price,
            "by_stock": wine.by_stock
        })
    return Response(dumped_wines)
