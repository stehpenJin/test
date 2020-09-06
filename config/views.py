from django.http import HttpResponse
from django.shortcuts import render
def welcom(request):
    html = "<html><body> welcom eh</body></html>"
    return HttpResponse(html)

def index(request):
    html = "<html><body>hi</body></html>"
    return HttpResponse(html)

def  template_test(request):
    return render(request, 'test.html')