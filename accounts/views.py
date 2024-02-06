from django.contrib.auth.views import LoginView, LogoutView

class MyLoginView(LoginView):
    template_name='accounts/login.html',
    redirect_autheticated_user='True',
