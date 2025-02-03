from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView



from employee.models import Employee

# Create your views here.
class EmployeeCreate(CreateView):
    model=Employee
    template_name='employee_form.html'
    fields = "__all__"    
    success_url="/list"

class EmployeeListView(ListView):
    template_name="employee_List.html"
    model=Employee
    def get_queryset(self):
        qs=Employee.objects.all()
        return qs
    
class EmployeeDetails(DetailView):
    model=Employee
    template_name="employee_Details.html"   

class EmployeeUpdate(UpdateView):
    model=Employee
    template_name='employee_form.html'
    fields="__all__"
    success_url="/list"

class EmployeeDelete(DeleteView):
    model=Employee
    success_url="/list"
    template_name="employee_confirm_delete.html"
    