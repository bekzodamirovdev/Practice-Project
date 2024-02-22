from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Account
from .serializers import RegisterSerializer


class AccountRegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = Account.objects.filter(email=user_data['email']).first()
        refresh = RefreshToken.for_user(user)


        user_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response({'success': True, 'data': user_data}, status=status.HTTP_201_CREATED)

class AccountListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer