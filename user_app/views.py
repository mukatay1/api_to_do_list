from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST', ])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', ])
def register_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()  # returning object of User ( __str__ -> self.username )
            data['username'] = account.username
            data['email'] = account.email
            data['response'] = 'Успешно регистрация прошла'
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
