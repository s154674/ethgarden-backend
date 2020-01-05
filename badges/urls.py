from django.urls import path
from badges import views

urlpatterns = [
    path('api/badges/', views.BadgeList.as_view()),
    path('api/badges/<str:owner>/', views.UserBadgeList.as_view()),
    path('api/badges/claim', views.ClaimBadge.as_view()),
]