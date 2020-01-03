from django.urls import path
from plants import views

urlpatterns = [
    path('plants/<str:owner>/', views.PlantList.as_view()),
    path('plant/<int:pk>/', views.PlantDetail.as_view()),
]