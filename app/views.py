from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.views.generic import View,TemplateView
# Create your views here.

class Data_render(View):
    def get(self,request):
        d={'name':'Amma Nanna'}
        return render(request,'data_render.html',d)


def insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)

        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data is inserted in FBV')
    return render(request,'insert_fbv.html',d)


class Cbv_insert(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Cbv_insert.html',d)

    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
        return HttpResponse('Cbv data is insert')


class Temp(TemplateView):
    template_name='temp.html'