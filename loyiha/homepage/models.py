from django.core.validators import FileExtensionValidator
from django.db import models
from account.models import Account


class Case(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    industry = models.CharField(max_length=221)
    description = models.TextField()
    viev = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=221)
    img = models.ImageField(upload_to='media/product/', null=True, blank=True)
    descript = models.CharField(max_length=221)

    def __str__(self) -> str:
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    video = models.FileField(upload_to='lesson_video/', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'mpeg', 'avi', 'flw', 'mov', 'mkv'])
    ])

    def __str__(self) -> str:
        return self.name


class Attendance(models.Model):
    student_id = models.ForeignKey(Account, on_delete = models.CASCADE, related_name = 'attendance_student_id')
    lesson_id = models.ForeignKey(Lesson, on_delete = models.CASCADE, related_name = 'attendance_lesson_id')
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.student_id.name
