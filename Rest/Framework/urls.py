from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('student/',StudentAPI.as_view()),
    path('register/',RegisterUser.as_view()),
    path('book',views.book,name="book"),
    # path('post',views.post_data,name="post_data"),
    # path('update_student/<id>/',views.update_student,name="update_stuent"),
    # path('delete_student/<id>/',views.delete_student,name="delete_stuent"),
]
