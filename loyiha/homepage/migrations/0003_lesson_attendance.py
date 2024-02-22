# Generated by Django 4.2.4 on 2024-02-21 11:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='lesson_video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mpeg', 'avi', 'flw', 'mov', 'mkv'])])),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_lesson_id', to='homepage.lesson')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_student_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]