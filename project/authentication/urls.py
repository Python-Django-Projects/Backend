from django.urls import  path


from .views import CustomUserList,CutomUserDetails,RegistrationView
# from .views import obt_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,  
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    
    path('user-list/', CustomUserList.as_view()),
    path('user-details/', CutomUserDetails.as_view()),
    
    path('register/', RegistrationView.as_view(), name='register'),
    
    # Token Authentication
    # path('api-token-auth/', obt_auth_token)

]