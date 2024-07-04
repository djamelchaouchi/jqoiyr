from django.urls import path
from .import views
from django.contrib import admin
from .views import home,chat,communities,calls


urlpatterns = [
path('', views.home, name='home' ),  #chats
path('communities', views.communities, name='communities' ),
path('status', views.status, name='status' ),
path('calls', views.calls, name='calls' ),
path('chat', views.chat, name='chat' ),
]