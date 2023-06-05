from django.urls import path
from . import views
from .views import UserList, TokenObtainPairView, login_view , logout_view, register_view

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.bot_list_view, name='bot_list'),
    path('create/', views.create_bot_view, name='create_bot'),
    path('delete/<int:pk>/', views.delete_bot_view, name='delete_bot'),
    path('editbot/<int:bot_id>/', views.edit_bot_view, name='edit_bot'),
    path('api/register/', UserList.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    
]