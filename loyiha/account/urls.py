from django.urls import path
from .views import AccountRegisterView, AccountListView
app_name = 'account'

urlpatterns = [
    path('register/', AccountRegisterView.as_view()),
    path('list', AccountListView.as_view())
]
