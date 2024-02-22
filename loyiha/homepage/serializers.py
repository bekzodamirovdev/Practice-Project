from .models import Case, Product, Lesson, Attendance
from rest_framework import serializers


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['id', 'user', 'name', 'image', 'industry', 'description']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image', 'descript')


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'date', 'video')


class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id', 'student_id', 'lesson_id', 'status')
