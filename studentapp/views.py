from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

# 🔹 Home Page View
def home(request):
    return render(request, "studentapp/home.html")

class StudentListView(ListView):
    model = Student
    template_name = 'studentapp/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'studentapp/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'roll_no', 'course', 'age']
    template_name = 'studentapp/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'roll_no', 'course', 'age']
    template_name = 'studentapp/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'studentapp/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
