from django.shortcuts import render, redirect, get_object_or_404
from .models import Bot
from .forms import BotForm
import telegram


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, TokenObtainPairSerializer


def home(request):
    return render(request, 'home.html')
@login_required
def bot_list_view(request):
    bots = Bot.objects.all()
    return render(request, 'bot_list.html', {'bots': bots})

@login_required
def create_bot_view(request):
    form = BotForm(request.POST or None)
    if form.is_valid():
        bot = form.save(commit=False)
        bot.save()
        bot_instance = telegram.Bot(bot.token)
        print(bot_instance.get_me())
        return redirect('bot_list')
    return render(request, 'bot_form.html', {'form': form})

def delete_bot_view(request, pk):
    bot = get_object_or_404(Bot, pk=pk)
    bot.delete()
    return redirect('bot_list')


def edit_bot_view(request, bot_id):
    bot = get_object_or_404(Bot, id=bot_id)
    if request.method == 'POST':
        bot.name = request.POST.get('name')
        bot.token = request.POST.get('token')
        bot.save()
        return redirect('bot_list')
    return render(request, 'edit_bot.html', {'bot': bot})

class UserList(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bot_list')
        else:
            error_message = 'Неправильные учетные данные'
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bot_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def send_message_view(request, bot_id):
    bot = get_object_or_404(Bot, id=bot_id)
    if request.method == 'POST':
        message = request.POST['message']
        bot.send_message(message)
    return render(request, 'send_message.html', {'bot': bot})