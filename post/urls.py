from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name="posts_list"),
    path('watch/<int:pk>', views.post_card, name='post_card')
]
