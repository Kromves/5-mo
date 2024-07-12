from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import RegistrationValidationSerializer, CodeValidationSerializer, \
    UserAuthenticationValidationSerializer
from .models import Code
from random import randint
from django.utils import timezone


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegistrationValidationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = User.objects.create_user(username=username, password=password, is_active=False)
            code = randint(100000, 999999)
            deadline = timezone.now() + timezone.timedelta(minutes=5)
            Code.objects.create(user=user, code=code, deadline=deadline)
            return Response(data={'code': code}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def confirm(request):
    if request.method == 'POST':
        serializer = CodeValidationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user_code = Code.objects.get(code=serializer.validated_data['code'])
            except Code.DoesNotExist:
                return Response(data={'error': 'Invalid code'}, status=status.HTTP_404_NOT_FOUND)

            if user_code.deadline < timezone.now():
                new_code = randint(100000, 999999)
                deadline = timezone.now() + timezone.timedelta(minutes=5)
                Code.objects.create(user=user_code.user, code=new_code, deadline=deadline)
                user_code.delete()
                return Response(data={'message': f'Code expired. New code sent: {new_code}'},
                                status=status.HTTP_201_CREATED)

            user_code.user.is_active = True
            user_code.user.save()
            user_code.delete()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = UserAuthenticationValidationSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(username=serializer.validated_data['username']).first()
            if user and user.check_password(serializer.validated_data['password']):
                token, created = Token.objects.get_or_create(user=user)
                return Response(data={'token': token.key}, status=status.HTTP_200_OK)
            return Response(data={'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)