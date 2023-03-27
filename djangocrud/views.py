from django.shortcuts import render,redirect
from employee.models import Employee

dic = {}

def home(request):
    data = Employee.objects.all()
    if request.method == "GET":
        sn = request.GET.get('search')
        if sn!= None:
            data = Employee.objects.filter(name__icontains = sn)
    dic['data'] = data
    return render(request,"index.html",dic)

def addData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employee(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
    return redirect('home')


def update(request,id):
     if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employee(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('home')

def delete(request,id):
    if request.method == "POST":
     Employee.objects.filter(id = id).delete()
    return redirect('home')

def deleteAll(request):
    if request.method == "POST":
        Employee.objects.all().delete()
    return redirect('home')
