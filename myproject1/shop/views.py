from django.http import HttpResponse
def home(request):
    return HttpResponse("shop home page")
def products(request):
    return HttpResponse("shop products page")