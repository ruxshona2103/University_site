from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')


@login_required_decorator
def home_page(requset):
    faculties = services.get_data_from_table("adminapp_faculty")
    kafedras = services.get_data_from_table("adminapp_kafedra")
    subjects = services.get_data_from_table("adminapp_subjects")
    teachers = services.get_data_from_table("adminapp_teachers")
    groups = services.get_data_from_table("adminapp_groups")
    students = services.get_data_from_table("adminapp_students")
    ctx = {
        'counts': {
            'faculties': len(faculties),
            'kafedras': len(kafedras),
            'subjects': len(subjects),
            'teachers': len(teachers),
            'groups': len(groups),
            'students': len(students),
        }
    }
    return render(requset, 'index.html', ctx)


@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect('faculty_list')


@login_required_decorator
def faculty_list(request):
    faculties = services.get_data_from_table("adminapp_faculty")
    print(faculties)
    ctx = {
        "faculties": faculties
    }
    return render(request, 'faculty/list.html', ctx)


# KAFEDRA
@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "form": form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return redirect('kafedra_list')


@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedra_with_faculty()
    ctx = {
        "kafedras": kafedras
    }
    return render(request, 'kafedra/list.html', ctx)


@login_required_decorator
def subject_create(request):
    model = Subjects()
    form = SubjectForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        'form': form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_edit(request, pk):
    model = Subjects.objects.get(pk=pk)
    form = SubjectForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, "subject/form.html", ctx)


@login_required_decorator
def subject_delete(request, pk):
    model = Subjects.objects.get(pk=pk)
    model.delete()
    return redirect('subject_list')


@login_required_decorator
def subject_list(request):
    subjects = services.get_data_from_table("adminapp_subjects")
    ctx = {
        'subjects': subjects
    }
    return render(request, 'subject/list.html', ctx)


# TEACHER
@login_required_decorator
def teacher_create(request):
    model = Teachers()
    form = TeachersForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("teacher_list")
    ctx = {
        "form": form
    }
    return render(request, "teacher/form.html", ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teachers.objects.get(pk=pk)
    form = TeachersForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("teacher_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "teacher/form.html", ctx)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teachers.objects.get(pk=pk)
    model.delete()
    return redirect("teacher_list")


@login_required_decorator
def teachers_list(request):
    teachers = services.get_teacher_with_details()
    ctx = {
        'teachers': teachers
    }
    return render(request, 'teacher/list.html', ctx)


@login_required_decorator
def group_create(request):
    model = Groups()
    form = GroupsForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx = {
        'form': form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_edit(request, pk):
    model = Groups.object.get(pk=pk)
    form = GroupsForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("teacher_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "group/form.html", ctx)


@login_required_decorator
def group_delete(request, pk):
    model = Groups.object.get(pk=pk)
    model.delete()
    return redirect("group_list")


@login_required_decorator
def group_list(request):
    group = services.get_group_with_details()
    ctx = {
        'groups': group
    }
    return render(request, 'group/list.html', ctx)


@login_required_decorator
def student_create(request):
    model = Students()
    form = StudentsForm(request.POST, request.FILES,  instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    else:
        print(form.errors)
    ctx = {
        'form':form,
        "model": model,

    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_edit(request, pk):
    model = Students.objects.get(pk=pk)
    form = StudentsForm(request.POST, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_delete(request, pk):
    model = Students.objects.get(pk=pk)
    model.delete()
    return redirect('student_list')


@login_required_decorator
def student_list(request):
    students = services.get_students_with_groups()
    ctx = {
        'students': students
    }
    return render(request, 'student/list.html', ctx)

@login_required_decorator
def profile(request):
    return render(request, "profile.html")
