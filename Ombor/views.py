from django.shortcuts import render, redirect

from .models import *


def hamma_talabalar(request):
    data={
        "students": Student.objects.all()
    }
    return render(request, "Students.html", data)


def Hamma_rejalar(request):

    if request.method=="POST":
        if request.POST.get("bajaril")=="on":
            n=True
        else:
            n=False
        Rejalar.objects.create(
            sarlavha=request.POST.get("sar"),
            sana=request.POST.get("sana"),
            batafsil_malumot=request.POST.get("b_m"),
            bajarilgan=n,
            Student=Student.objects.get(id=request.POST.get("student")),
        )

    data={
        "students": Student.objects.all(),
        "rejalar": Rejalar.objects.all()
    }
    return render(request, "Rejalar.html", data)

def Bajarilmagan(request):

    data={
        "rej": Rejalar.objects.filter(bajarilgan=False)
    }
    return render(request, "Bajarilmagan.html", data)

def kamida_3_kurs(request):

    data={
        "talaba": Student.objects.filter(kurs__gte=3)
    }
    return render(request, "3_dan.html", data)



def rejani_ochir(request, pk):
    Rejalar.objects.get(id=pk)

    return redirect("/rejalar/")