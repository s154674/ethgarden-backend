from django.urls import path
from badges import views

urlpatterns = [
    path('badges/', views.BadgeList.as_view()),
    path('badges/<str:owner>/', views.UserBadgeList.as_view()),
    path('badges/claim', views.ClaimBadge.as_view()),
]