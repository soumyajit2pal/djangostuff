from django.shortcuts import render,redirect
from crudapplication.form import EmployeeForm
from crudapplication.models import Employee

def emp(request):
    
    if request.method =="POST":
        form=EmployeeForm(request.POST)
        print("yes")
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        
        form=EmployeeForm()
        print("No")
    return render(request,'crudapplication/index.html',{'form':form})


def show(request):
    employees=Employee.objects.all()
    return render(request,"crudapplication/show.html",{'employees':employees})

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'crudapplication/edit.html',{'employee':employee})

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'crudapplication/edit.html',{'employee':employee})

def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')