
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:repo_id>/repo", views.repo, name="repo"),
    url('', include('social_django.urls', namespace='social'))

]
