from django.http import HttpResponse

def homepage(request):
    return HttpResponse('This is our homepage')

def about(request):
    return HttpResponse('This is the about page')

