from django.shortcuts import render
from .models import Student

def form(request):
    if request.method == "POST":
        Student.objects.create(
            student_id=request.POST['student_id'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            major=request.POST['major'],
            phone=request.POST['phone']
        )
        return render(request, "myapp/form.html", {"msg": "บันทึกข้อมูลแล้ว!"})

    return render(request, "myapp/form.html")

def show(request):
    students = Student.objects.all()
    return render(request, "myapp/show.html", {"students": students})
