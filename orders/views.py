from django.http import HttpResponse

def order_list(request):
    return HttpResponse("لیست سفارش‌ها - تست")

def order_detail(request, pk):
    return HttpResponse(f"سفارش شماره {pk} - تست")
