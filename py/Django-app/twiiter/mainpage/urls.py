from django.urls import path
from mainpage import views

urlpatterns=[
    path('post/', views.post_list)
]