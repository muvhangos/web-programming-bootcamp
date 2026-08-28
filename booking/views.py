from django.shortcuts import render, redirect
from .models import Booking

def home(request):
    if request.method == "POST":
        Booking.objects.create(
            customer_name=request.POST["customer_name"],
            service=request.POST["service"],
            booking_date=request.POST["booking_date"],
        )
        return redirect("success")

    return render(request, "booking/home.html")

def success(request):
    return render(request, "booking/success.html")
