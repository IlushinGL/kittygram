from django.urls import path # , include

from cats.views import CatList, CatDetail

urlpatterns = [
    path('cats/', CatList.as_view()),
    path('cats/<int:pk>/', CatDetail.as_view()),
] 
