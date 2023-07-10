from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def full(request):
    return render(request,'blog-home.html')
def new(request):
    return render(request,'blog-post.html')
def old(request):
    return render(request,'contact.html')
def majina(request):
    return render(request,'faq.html')
def magari(request):
    return render(request,'about.html')
def copy(request):
    return render(request,'portfolio-item.html')
def paste(request):
    return render(request,'portfolio-overview.html')
def renew(request):
    return render(request,'pricing.html')

