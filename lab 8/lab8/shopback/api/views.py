from django.http.response import JsonResponse
from api.models import get_all_categories, get_all_products



def product_list(request):
    products_json = [p.to_json() for p in get_all_products()]
    return JsonResponse(products_json, safe=False)


def product_details(request, product_id):
    for product in get_all_products():
        if product.id == product_id:
            return JsonResponse(product.to_json(), safe=False)
    return JsonResponse({'error': 'Product not found'})


def products_by_category(request, category_id):
    products_json = [p.to_json() for p in get_all_products() if p.category_id == category_id]
    return JsonResponse(products_json, safe=False)


def categories_list(request):
    categories_json = [c.to_json() for c in get_all_categories()]
    return JsonResponse(categories_json, safe=False)


def categories_details(request, category_id):
    for category in get_all_categories():
        if category.id == category_id:
            return JsonResponse(category.to_json(), safe=False)
    return JsonResponse({'error': 'Product not found'})
