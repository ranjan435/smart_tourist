from django.urls import path,include
from .views import index,recommend,detail,search_recommend

urlpatterns = [
    path('',index,name='home'),
    path('recommend',recommend,name='recommend'),
    path('place/<int:place_id>', detail, name='detail'),
    path('search', search_recommend, name='search'),
]