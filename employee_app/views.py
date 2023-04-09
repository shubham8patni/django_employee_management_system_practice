from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Departement
from datetime import datetime
from .forms import AddEmpFrom
# Create your views here.

def index(request):
    return render(request, 'index.html')


def view_all_emp(request):
    emps = Employee.objects.all()
    context = {
        "emps" : emps
    }
    return render(request, 'view_all_emp.html', context= context)

# Using self built form
# def add_emp(request):
#     if request.method == "POST":
#         print(request.POST)
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         department = int(request.POST['department'])
#         role = int(request.POST['role'])
#         salary = int(request.POST['salary'])
#         phone_number = int(request.POST['phone_number'])
#         bonus = int(request.POST['bonus'])
#         new_emp = Employee(first_name = first_name, last_name = last_name, dept_id = department, role_id = role, salary = salary, bonus = bonus, phone_number = phone_number, hire_date = datetime.now())
#         new_emp.save()
#         return HttpResponse('Employee added successfully!')
#     elif request.method == "GET":
#         return render(request, 'add_emp.html')
#     else:
#         return HttpResponse('An exception orccured!')


# Using django forms
def add_emp(request):
    if request.method == "POST":
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = int(request.POST['department'])
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        phone_number = int(request.POST['phone_number'])
        bonus = int(request.POST['bonus'])
        new_emp = Employee(first_name = first_name, last_name = last_name, dept_id = department, role_id = role, salary = salary, bonus = bonus, phone_number = phone_number, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully!')
    elif request.method == "GET":
        form = AddEmpFrom()
        # rendered_form = form.render("add_emp.html")
        context = {"form" : form}
        return render(request, 'add_emp.html', context)
    else:
        return HttpResponse('An exception orccured!')


def rem_emp(request):
    if request.method == 'GET':
        emps = Employee.objects.all()
        context = {
            "emps" : emps
        }    
        return render(request, 'rem_emp.html', context= context)
    elif request.method == "POST" : 
       print(request.POST)
       employee_id = int(request.POST['emp_id'])
       employee_to_be_removed = Employee.objects.get(id = employee_id)
       employee_to_be_removed.delete()
       return HttpResponse('Employee removed successfully!')
    else:
        return HttpResponse('An exception orccured!')
 
