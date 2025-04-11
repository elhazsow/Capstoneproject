from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns =[
    path('', views.index, name='home'),
    path('menu/', views.MenuItemAPIView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]