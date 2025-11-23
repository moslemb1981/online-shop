from django.http import HttpResponse

def product_list(request):
    return HttpResponse("لیست محصولات - تست")

def product_detail(request, pk):
    return HttpResponse(f"جزئیات محصول {pk} - تست")
