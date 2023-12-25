from django.urls import path
from .views import (
    teacher_form,
    teachers_list,
    teacher_edit,
    teacher_delete,
    group_form,
    group_edit,
    groups_list,
    group_delete,
    student_form,
    student_list,
    student_edit,
    student_delete,
)

urlpatterns = [
    path("teacher/", teacher_form, name="teacher_form"),
    path("teacher/<int:pk>", teacher_edit, name="teacher_edit"),
    path("teachers/", teachers_list, name="teacher_list"),
    path("group/", group_form, name="group_form"),
    path("groups/", groups_list, name="group_list"),
    path("group/<int:pk>", group_edit, name="group_edit"),
    path("student/", student_form, name="student_form"),
    path("students/", student_list, name="student_list"),
    path("student/<int:pk>", student_edit, name="student_edit"),
    path("teacher/<int:pk>/delete/", teacher_delete, name="teacher_delete"),
    path("group/<int:pk>/delete/", group_delete, name="group_delete"),
    path("student/<int:pk>/delete/", student_delete, name="student_delete"),
]
