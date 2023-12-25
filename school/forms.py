import phonenumbers
from django import forms
from django.core.exceptions import ValidationError

from school.models import Teachers, Groups, Students


class TeacherForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Groups.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Teachers
        fields = ["full_name", "date_of_birth", "photo", "groups"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["groups"].initial = self.instance.groups.all()

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"]
        if len(full_name) > 30:
            raise forms.ValidationError(
                "ПІБ занадто довге. Максимальна довжина 30 символів."
            )
        return full_name


class GroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ["name", "teacher"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) > 10:
            raise forms.ValidationError(
                "Назва занадто довга. Максимальна довжина 10 символів."
            )
        return name


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ["full_name", "year", "phone", "group"]

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone:
            raise forms.ValidationError("Введіть номер телефону.")
        try:
            parsed = phonenumbers.parse(phone, None)
        except phonenumbers.NumberParseException as e:
            raise forms.ValidationError(e.args[0])
        return phonenumbers.format_number(
            parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"]

        if any(char.isdigit() for char in full_name):
            raise ValidationError("Ім'я не повинно містити цифри.")
        if len(full_name) > 30:
            raise ValidationError("Довжина імені не повинна перевищувати 30 символів.")

        return full_name
