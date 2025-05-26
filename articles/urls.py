from debug_toolbar.urls import app_name
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list),
    path('<slug:slug>/', views.article_details, name='article_details'),
]