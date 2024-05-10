from django.urls import path

from app_user.views import register_view, login_view, logout_view, profile_view, email_verification, change_password, \
    user_delete, change_email

app_name = 'app_user'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('email_verification/<str:email>/<uuid:code>/', email_verification, name='email_verification'),
    path('change-password/', change_password, name='change_password'),
    path('user-delete/', user_delete, name='user_delete'),
    path('change-email/', change_email, name='change_email'),
]
