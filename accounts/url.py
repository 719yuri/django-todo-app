
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

#カッコが閉じられてないとエラーになる。LogoutViewのインポートがうまくいっていない？もしくは継承がうまくいっていない？#
urlpatterns = [ 
    path(
      "login/",
      LoginView.as_view(
          template_name="accounts/login.html",
          redirect_autheticated_user=True,
      ),
      name="login",
    )
    path(
      "logout/",
      LogoutView.as_view(),
      name="logout"
    )
]

