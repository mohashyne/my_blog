from django.urls import path

from articles.urls import app_name, urlpatterns
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup")
]