from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from .forms import TeacherForm, GroupForm, StudentForm

from .models import Teachers, Groups, Students


def teacher_form(request):
    teacher = Teachers()
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teacher_form.html", {"form": form})
    form = TeacherForm(request.POST, request.FILES, instance=teacher)
    if form.is_valid():
        teacher = form.save()
        selected_groups = form.cleaned_data["groups"]
        teacher.groups.set(selected_groups)
        return redirect(reverse("teacher_list"))

    return render(request, "teacher_edit.html", {"form": form})


def teacher_edit(request, pk):
    teacher = Teachers.objects.get(pk=pk)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teacher_edit.html", {"form": form, "teacher": teacher})
    form = TeacherForm(request.POST, request.FILES, instance=teacher)
    if form.is_valid():
        teacher = form.save()
        selected_groups = form.cleaned_data["groups"]
        teacher.groups.set(selected_groups)
        return redirect(reverse("teacher_edit", kwargs={"pk": teacher.pk}))

    return render(request, "teacher_edit.html", {"form": form, "teacher": teacher})


def teachers_list(request):
    teachers = Teachers.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})


def teacher_delete(request, pk):
    try:
        teacher = Teachers.objects.get(pk=pk)
        teacher.delete()
        return redirect(reverse("teacher_list"))
    except ProtectedError:
        message = "Цей вчитель має зв'язки і не може бути видалений."
        return HttpResponse(message, status=400)


def group_form(request):
    if request.method == "GET":
        form = GroupForm()
        return render(request, "group_form.html", {"form": form})

    form = GroupForm(request.POST)
    if form.is_valid():
        group = form.cleaned_data["name"]
        teacher = form.cleaned_data["teacher"]

        group, created = Groups.objects.get_or_create(
            name=group, defaults={"teacher": teacher}
        )

        if not created:
            group.teacher = teacher
            group.save()

        return redirect(reverse("group_list"))

    return render(request, "group_form.html", {"form": form})


def group_edit(request, pk):
    group = Groups.objects.get(pk=pk)
    if request.method == "GET":
        form = GroupForm(instance=group)
        return render(
            request, "group_edit.html", {"form": form, "group": group}
        )  # Добавьте "group" в контекст
    form = GroupForm(request.POST, instance=group)
    if form.is_valid():
        form.save()
        redirect(reverse("group_edit", args=[form.instance.pk]))

    return redirect(reverse("group_edit", args=[form.instance.pk]))


def groups_list(request):
    groups = Groups.objects.all()
    return render(request, "group_list.html", {"groups": groups})


def group_delete(request, pk):
    try:
        group = Groups.objects.get(pk=pk)
        group.delete()
        return redirect(reverse("group_list"))
    except ProtectedError:
        message = "Ця група має зв'язки і не може бути видалена."
        return HttpResponse(message, status=400)


def student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "student_form.html", {"form": form})
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("student_list"))

    return render(request, "student_form.html", {"form": form})


def student_list(request):
    students = Students.objects.all()
    return render(request, "student_list.html", {"students": students})


def student_edit(request, pk):
    student = Students.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "student_edit.html", {"form": form, "student": student})
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        redirect(reverse("student_edit", args=[form.instance.pk]))

    return redirect(reverse("student_edit", args=[form.instance.pk]))


def student_delete(request, pk):
    try:
        student = Students.objects.get(pk=pk)
        student.delete()
        return redirect(reverse("student_list"))
    except ProtectedError:
        message = "Цей студент має зв'язки і не може бути видалений."
        return HttpResponse(message, status=400)
