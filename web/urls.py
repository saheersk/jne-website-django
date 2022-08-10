from django.urls import path
from web import views


app_name = "web"


urlpatterns = [
    path('', views.index, name='index'),
    path('application/', views.form, name='form'),
    path('application/download/', views.download, name='download'),
]