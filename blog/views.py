from django.http import HttpResponse

def blog_list(request):
    return HttpResponse("لیست مقالات - تست")

def blog_detail(request, pk):
    return HttpResponse(f"مقاله شماره {pk} - تست")
