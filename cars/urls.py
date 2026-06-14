from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
    path('post', views.post_car, name='post_car'),
    path('delete/<int:id>', views.delete_car, name='delete_car'),
]
