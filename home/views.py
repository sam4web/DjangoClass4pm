from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    views = dict()
    views["feedbacks"] = Feedback.objects.all()
    return render(request, "index.html", views)


def about(request):
    return render(request, "about.html")


def portfolio(request):
    return render(request, "portfolio.html")


def price(request):
    return render(request, "price.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    views = dict()
    views["information"] = Information.objects.all()

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        data = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        data.save()
        views["message"] = "Your message is sent!"
        return render(request, "contact.html", views)
    return render(request, "contact.html", views)
