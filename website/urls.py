from django.urls import path,include
from . import  views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('get_chatbot_response/', views.get_chatbot_response, name='chatbot_response')
]