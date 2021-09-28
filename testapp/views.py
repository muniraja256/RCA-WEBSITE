from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def get_in_touch(request):
    return render(request,'get_in_touch.html')