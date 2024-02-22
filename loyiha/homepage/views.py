from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from .models import Case, Product, Lesson, Attendance
from .serializers import CaseSerializer, ProductSerializers, ProductCreateSerializers, LessonSerializers, AttendanceSerializers
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser


class CaseView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q) 
        return qs


class CaseCreateViev(generics.CreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CaseRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = CaseSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Case.objects.all()
    
    def retrieve(self, request, *a, **k):
        instance = self.get_object()
        instance.viev += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CaseUpdateView(generics.UpdateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [IsOwnerOrReadOnly]


@api_view(['POST'])
def create_product(request):
    serializer = ProductCreateSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # 201 Created
    return Response(serializer.errors, status=400)  # 400 Bad Request


@api_view(['GET'])
def ProductView(request):
    queryset = Product.objects.all()
    serializer = ProductSerializers(queryset, many=True)  # Instantiate serializer with queryset

    if serializer.is_valid():
        return Response(serializer.data)  # Return Response with serializer data

    return Response({'message': 'Queryset is not found'})


class LessonListCreateApiView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


class AttendanceListCreateApiView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers


class AttendanceRetrieveView(generics.RetrieveAPIView):
    serializer_class = AttendanceSerializers
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Attendance.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        sz = self.get_serializer(instance)
        return Response(sz.data, status=status.HTTP_200_OK)


