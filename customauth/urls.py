from django.urls import path
from customauth import views

urlpatterns = [
    path('api/token', views.ObtainTokenPairView.as_view()),
    # path('api/refresh', views.RefreshTokenView.as_view()),
    path('api/tokensig', views.SignatureObtainTokenPairView.as_view()),
]