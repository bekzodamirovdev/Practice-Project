from django.urls import path
from .views import CaseView, CaseRetrieveApiView, CaseCreateViev, CaseUpdateView, ProductView, create_product, LessonListCreateApiView, AttendanceRetrieveView, AttendanceListCreateApiView

urlpatterns = [
    path('case/', CaseView.as_view(), name='case'),
    path('case-create/', CaseCreateViev.as_view(), name='case-create'),
    path('case-retrieve/<int:pk>/', CaseRetrieveApiView.as_view(), name='case-retrieve'),
    path('case-update/<int:pk>/', CaseUpdateView.as_view(), name='case-update'),
    path('product/', ProductView),
    path('product-create', create_product),
    path('lesson-create', LessonListCreateApiView.as_view(), name='lesson-create'),
    path('attendance-create', AttendanceListCreateApiView.as_view(), name='lesson-create'),
    path('attendance-retrieve/<int:pk>/', AttendanceRetrieveView.as_view(), name='lesson-retrieve'),
]
