from django.urls import path
from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', views.top, name='top'),
    path('works/', views.works, name='works'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('form/', views.Form.as_view(), name='form'),
    path('thanks/', views.Thanks.as_view(), name='thanks'),
]