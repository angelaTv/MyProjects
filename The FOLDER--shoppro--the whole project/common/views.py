from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, "common/index.html")


def about_page(request):
    return render(request, "common/about.html")


def contact_page(request):
    return render(request, "common/contact.html")
