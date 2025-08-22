from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import request
from django.core.mail import send_mail

def Home_page(request):
    if request.method == 'POST':
        message_email = request.POST.get('message_email')
        message_name = request.POST.get('message_name')
        message = request.POST.get('message')
        
        send_mail(
           subject= message_name,
           message= f"{message_name} Sent me this message:\n{message}\n And their email is:  {message_email}",
            from_email= message_email,
            recipient_list=['boulahdourabdelmalek@gmail.com'],
        )
        messages.success(request, "Your Email was sent succusfully!")
        return render(request, 'Home/home.html')
    else:
        return render(request, 'Home/home.html')
