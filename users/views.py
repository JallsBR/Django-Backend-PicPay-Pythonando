import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from rest_framework import generics
from users.serializers import UserSerializer
from django.contrib.auth.hashers import make_password


class Signup(generics.GenericAPIView):
    serializer_class = UserSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data.get('username')
        last_name = data.get('last_name')
        email = data.get('email')
        cpf = data.get('cpf')
        password = data.get('password')
        
        if not username or not last_name or not email or not cpf or not password:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)

        if User.objects.filter( cpf=cpf.replace('.', '').replace('-', '')).exists():
            return JsonResponse({'error': 'CPF already exists'}, status=400)

        user = User(
            username=username,
            last_name=last_name,
            email=email,
            cpf=cpf,
            password= make_password(password) )
        try:            
            user.full_clean()
            user.save()
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

        return JsonResponse({'message': 'User created successfully'}, status=201)
    
    