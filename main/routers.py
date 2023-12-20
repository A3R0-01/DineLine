from rest_framework import routers
from main.user.viewsets import UserViewSet
from main.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from main.tables.viewsets import TableViewSet, RegisterTableViewSet


router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register' )
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'table', TableViewSet, basename='table')
router.register(r'tables/register', RegisterTableViewSet, basename='table-register')
urlpatterns = [
    *router.urls,
]