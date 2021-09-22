from django import forms
from django.shortcuts import redirect, render
from .forms import SupportForm
from django.http import HttpRequest, HttpResponse
from .models import Callback



def main_view(request): 
    context = {}
    form = SupportForm(request.POST or None)
    context['form'] = form 
    if request.method == "POST": 
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            problem_desc = form.cleaned_data["subject"]
            date_and_time = form.cleaned_data["date_and_time"]
            temp = Callback(name = name,phone_number = phone_number ,email = email ,subject = subject ,problem_desc = problem_desc,date_and_time = date_and_time)
            temp.save()
            return HttpResponse("Your problem was successfully proceeded! We'll respond as soon as possible!") 

    return render(request, "main.html", context)

def index_view(request): 
    return redirect("/home/")

 
