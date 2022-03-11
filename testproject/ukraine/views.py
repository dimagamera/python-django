from django.http import HttpResponse

def index(request):
    print(request)
    return HttpResponse('<h1>No War In Ukraine</h>')
def test(request):
    return HttpResponse('<h1>Putin Huilo</h>')