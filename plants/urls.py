from django.urls import path
from plants import views

urlpatterns = [
    path('api/plants/<str:owner>/', views.PlantList.as_view()),
    path('api/plant/<int:pk>/', views.PlantDetail.as_view()),
]