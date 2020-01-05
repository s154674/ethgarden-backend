from django.urls import path
from customauth import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/token/', views.ObtainTokenPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/tokensig/', views.SignatureObtainTokenPairView.as_view()),
    path('api/users/<str:public_address>/', views.UserDetail.as_view()),
    path('api/users/<str:public_address>/greens', views.GreenDetial.as_view()),
]