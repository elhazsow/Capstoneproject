from . import views
from django.urls import path



urlpatterns =[
    path('', views.index, name='home'),
    path('menu/', views.MenuItemAPIView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemAPIView.as_view()),
]