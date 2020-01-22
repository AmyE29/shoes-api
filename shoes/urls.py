from django.urls import path
from .views import ShoesList, ShoesDetail 

urlpatterns = [
    path('shoe/', ShoesList.as_view(), name= 'shoes_list'),
    path('shoe/<int:pk>/', ShoesDetail.as_view(), name= 'shoes_detail')

]