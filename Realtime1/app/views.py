from django.shortcuts import render,redirect
from .models import Register
from .models import hotal
from .models import Room
from .models import Calculetar
from .models import Login
import re
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView
# Create your views here.
#def index(request):
 #   return render(request,"index.html")


def send(request):
    name=request.POST.get("name")
    surname=request.POST.get("surname")
    date=request.POST.get("date")
    gen=request.POST.get("gen")
    phone = request.POST.get("phone")
    password = request.POST.get("password")
    Repassword = request.POST.get("Repassword")
    gmail=request.POST.get("gmail")
    a=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",gmail)
    if a!=None:
        Register(name=name,surname=surname,date=date,gen=gen,gmail=gmail,phone=phone,password=password,Repassword=Repassword).save()
        return render(request,"hotal.html",{"message":"Successfull Register"})
    else:
        return render(request, "show.html", {"message": "Invalid"})



def index1(request):
    name = request.POST.get("name")
    age= request.POST.get("age")
    phone = request.POST.get("phone")
    std = request.POST.get("std")
    end=request.POST.get("end")
    Room=request.POST.get("Room")
    hotal(name=name, age=age, phone=phone, std=std, end=end, Room=Room).save()
    return render(request, "Rho.html")



def index2(request):
    return render(request,"images.html")


class Index(CreateView):
    model = Room
    template_name = "index1.html"
    fields = ["Room","phone"]
    success_url = "/show/"


class Update(UpdateView):
    model = Room
    template_name = "update.html"
    fields = ["Room","phone"]
    success_url ="/show/"


class Dpdate(DeleteView):
    model = Room
    template_name = "delete.html"
    fields = ["Room","phone"]
    success_url = "/show/"

def borde(request):
    year=request.POST.get("year")
    month=request.POST.get("month")
    Ammount=request.POST.get("Ammount")
    result=request.POST.get("result")
    Calculetar(year=year,month=month,Ammount=Ammount,result=result).save()
    return render(request,"Borde.html")


def vaild(request):
    if request.method=="POST":
        gmail=request.POST.get("gmail")
        password=request.POST.get("password")
        qs=Register.objects.filter(gmail=gmail,password=password)
        if qs:
            request.session["gm"]=gmail
            return render(request,"hotal.html")
        else:
            return render(request,"Html.html",{"message":"Plase Send You Detalis And Register"})


def logout1(request):
    del request.session["gm"]
    request.session.modified=True
    return redirect("/index/")


