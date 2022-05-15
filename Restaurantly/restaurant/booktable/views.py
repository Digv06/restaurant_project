from email import message
from django.shortcuts import render
from .models import Contact,Booking

# Create your views here.
def index(request):
    return render(request, 'booktable/index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'booktable/contact.html')

def tablebooking(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        people = request.POST.get('people', '')
        message = request.POST.get('message', '')
        book = Booking(name=name, email=email, date=date, time=time, people=people, message=message)
        book.save()
    return render(request, 'booktable/tablebooking.html')