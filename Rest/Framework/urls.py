from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('generic-student/',StudentGeneric.as_view()),
    path('generic-student/<id>/',GenericUpdate.as_view()),
    path('student/',StudentAPI.as_view()),
    path('register/',RegisterUser.as_view()),
    path('book',views.book,name="book"),
]
