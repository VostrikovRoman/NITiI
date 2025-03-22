from django.shortcuts import render,redirect
from .models import Students
from .forms import StudentsForm
from django.views.generic import DetailView, UpdateView, DeleteView

def students (request):
    s=request.GET.get('search','')
    students = Students.objects.filter(surname__icontains = s).order_by('surname')
    return render(request, 'students/students.html', {'students':students})

class Student_Page(DetailView):
    model = Students
    template_name = 'students/student_page.html'
    context_object_name = 'student'

class Update(UpdateView):
    model = Students
    template_name = 'students/update.html'
    form_class = StudentsForm

class Delete(DeleteView):
    model = Students
    success_url = '/students/'
    template_name = 'students/delete.html'
    

def add (request):
    error = ''
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        form = StudentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')
        else:
            form = StudentsForm()
            error = 'Данные заполнены неверно'    
    form = StudentsForm()
    return render(request, 'students/add.html', {'form':form, 'error':error})

def Search (request):
    s=request.GET['text']