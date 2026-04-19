from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostCreateView, PostViewSet, ProfileViewSet, ThrottledTokenObtainPairView, UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register('profiles', ProfileViewSet, basename='profiles')
router.register('posts', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/posts/create/', PostCreateView.as_view(), name='post-create'),
    path('api/token/', ThrottledTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
