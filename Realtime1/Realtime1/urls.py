"""Realtime1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from app.models import Room

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("index/", views.index),
    path("index/",TemplateView.as_view(template_name="index.html"),name="index"),
    path("send/", views.send),
    path("index1/", TemplateView.as_view(template_name="hotal.html"), name="hotal"),
    path("index2/",views.index1),
    path("index3/",views.index2),
    path("index4/", TemplateView.as_view(template_name="images.html"), name="images1"),
    path("index5/",views.Index.as_view()),
    path("show/",ListView.as_view(template_name="List.html",model=Room),name="Ram"),
    path("update<int:pk>/",views.Update.as_view()),
    path("delete<int:pk>/",views.Dpdate.as_view()),
    path("index6/",TemplateView.as_view(template_name="Borde.html"),name="Borde"),
    path("Borde/",views.borde),
    path("login/",TemplateView.as_view(template_name="Login.html"),name="login"),
    path("valid/",views.vaild,name="valid"),
    path("logout/",TemplateView.as_view(template_name="logout.html"),name="logout"),
    path("logout1/",views.logout1,name="logout1"),
    path("index7/",TemplateView.as_view(template_name="index7.html"),name="index7"),
    path("index8/",TemplateView.as_view(template_name="index8.html"),name="index8"),
    path("index9/",TemplateView.as_view(template_name="index9.html"),name="index9"),
    path("index10/",TemplateView.as_view(template_name="index10.html"),name="index10"),
    path("index11/",TemplateView.as_view(template_name="index11.html"),name="index11"),
    path("index12/",TemplateView.as_view(template_name="index12.html"),name="index12"),
    path("index13/",TemplateView.as_view(template_name="index13.html"),name="index13"),
    path("index14/",TemplateView.as_view(template_name="index14.html"),name="index14"),
    path("index15/",TemplateView.as_view(template_name="index15.html"),name="index15"),
    path("index16/",TemplateView.as_view(template_name="index16.html"),name="index16"),
    path("index17/",TemplateView.as_view(template_name="index17.html"),name="index17"),
    path("index18/",TemplateView.as_view(template_name="index18.html"),name="index18"),
    path("index19/",TemplateView.as_view(template_name="index19.html"),name="index19"),
    path("index20/",TemplateView.as_view(template_name="index20.html"),name="index20"),
    path("index21/",TemplateView.as_view(template_name="index21.html"),name="index21"),
    path("index22/",TemplateView.as_view(template_name="index22.html"),name="index22"),
    path("index23/",TemplateView.as_view(template_name="index23.html"),name="index23"),
    path("index24/",TemplateView.as_view(template_name="index24.html"),name="index24"),
    path("index25/",TemplateView.as_view(template_name="index25.html"),name="index25"),
    path("index26/",TemplateView.as_view(template_name="index26.html"),name="index26"),
    path("index27/",TemplateView.as_view(template_name="index27.html"),name="index27"),
    path("index28/",TemplateView.as_view(template_name="index28.html"),name="index28"),
    path("index29/",TemplateView.as_view(template_name="index29.html"),name="index29"),
    path("index30/",TemplateView.as_view(template_name="index30.html"),name="index30"),
    path("index31/",TemplateView.as_view(template_name="index31.html"),name="index31"),
    path("index32/",TemplateView.as_view(template_name="index32.html"),name="index32"),
    path("index33/",TemplateView.as_view(template_name="index33.html"),name="index33"),
    path("index34/",TemplateView.as_view(template_name="index34.html"),name="index34"),
    path("index35/",TemplateView.as_view(template_name="index35.html"),name="index35"),
    path("index36/",TemplateView.as_view(template_name="index36.html"),name="index36"),
    path("index37/",TemplateView.as_view(template_name="index37.html"),name="index37"),
    path("index38/",TemplateView.as_view(template_name="index38.html"),name="index38"),
    path("index39/",TemplateView.as_view(template_name="index39.html"),name="index39"),
    path("index40/",TemplateView.as_view(template_name="index40.html"),name="index40"),
    path("index41/",TemplateView.as_view(template_name="index41.html"),name="index41"),
    path("index42/",TemplateView.as_view(template_name="index42.html"),name="index42"),
    path("index43/",TemplateView.as_view(template_name="index43.html"),name="index43"),
    path("index44/",TemplateView.as_view(template_name="index44.html"),name="index44"),
    ]


