from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('sign-up/', views.sign_up, name="sign_up"),
    path('delete-account', views.delete_account, name="delete_account"),
    path('password-reset', views.password_reset_request, name="password_reset_request"),
    path('new-password', views.new_password, name="new_password"),

]