# Generated by Django 4.2.7 on 2023-12-24 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0005_students_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="teachers",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="teachers"),
        ),
    ]