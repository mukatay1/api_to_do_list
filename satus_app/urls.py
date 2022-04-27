from django.urls import path
from .views import *

urlpatterns = [
    path('current/', CurrentList.as_view(), name='current_list'),
    path('current/<int:pk>/', CurrentDetail.as_view(), name='current_detail'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('list/', ListView.as_view(), name='list_list'),
    path('list/<int:pk>/', ListDetailView().as_view(), name='list_detail'),

]
