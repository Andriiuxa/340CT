from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Random Page For Test</h1>")