from django.http import HttpResponse

def hi(request):
    return HttpResponse('<h1>Hello Raspberry Pi!')

