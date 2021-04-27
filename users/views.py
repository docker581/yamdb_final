from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenViewBase

from .models import User
from .permissions import IsAdmin
from .serializers import TokenSerializer, UserSerializer


class EmailAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        username = email.split('@')[0]
        user, created = User.objects.get_or_create(
            username=username,
            email=email,
            is_active=False,
        )
        confirmation_code = default_token_generator.make_token(user)
        user.confirmation_code = confirmation_code
        user.save()
        send_mail(
            f'User with email {email}',
            f'Your confirmation_code is {confirmation_code}',
            'from@api.com',
            [email],
            fail_silently=False,
        )
        return Response({'confirmation_code': confirmation_code})


class TokenView(TokenViewBase):
    serializer_class = TokenSerializer


@permission_classes([IsAuthenticated, IsAdmin])
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'username'
    filter_backends = [SearchFilter]
    search_fields = ['username']

    @action(
        methods=['get', 'patch'],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path='me',
        url_name='personal_data',
    )
    def personal_data(self, request):
        user = User.objects.get(username=request.user.username)
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
