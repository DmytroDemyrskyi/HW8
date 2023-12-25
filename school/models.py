from django.db import models


class Teachers(models.Model):
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to="teachers", null=True, blank=True)
    group = models.ForeignKey(
        "Groups",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="teachers",
    )

    def __str__(self):
        return f"ID: {self.pk} {self.full_name} {self.date_of_birth}"


class Groups(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(
        Teachers, on_delete=models.PROTECT, related_name="groups"
    )

    def __str__(self):
        return f"ID: {self.pk} {self.name} {self.teacher}"


class Students(models.Model):
    full_name = models.CharField(max_length=50)
    year = models.IntegerField()
    phone = models.CharField(max_length=50, null=True)
    group = models.ForeignKey(Groups, on_delete=models.PROTECT, related_name="students")

    def __str__(self):
        return f"ID: {self.pk} FullName: {self.full_name} (Year: {self.year})"


class StudentGroup(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
