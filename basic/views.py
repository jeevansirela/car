from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'basic/home.html')

def test(request):
  return render(request, 'basic/test.html')