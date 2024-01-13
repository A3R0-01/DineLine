from rest_framework import routers
from main.user.viewsets import UserViewSet
from main.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from main.tables.viewsets import TableViewSet, RegisterTableViewSet
from main.customers.viewsets import CustomerViewset
from main.categories.viewsets import CategoryViewset
from main.menu.viewsets import MenuFilterViewSet, MenuViewSet
from main.orders.viewsets import OrdersMainViewSet
from main.foodorders.viewsets import FoodOrderCreateViewSet
from main.clearance.viewsets import ClearanceOneViewSet, ClearanceViewSet


router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register' )
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'table', TableViewSet, basename='table')
router.register(r'tables/register', RegisterTableViewSet, basename='table-register')
router.register(r'customer', CustomerViewset, basename='customer')
router.register(r'category', CategoryViewset, basename='categories')
router.register(r'categorymenu', MenuFilterViewSet, basename='menu-filter')
router.register(r'menu', MenuViewSet, basename='menu-all')
router.register(r'order', OrdersMainViewSet, basename='orders-main')
router.register(r'foodorder', FoodOrderCreateViewSet, basename='foodorder-edit')
router.register(r'clearance', ClearanceViewSet, basename='clearance-read')
router.register(r'clearance/customer', ClearanceOneViewSet, basename='clearance-read-customer')

urlpatterns = [
    *router.urls,
]