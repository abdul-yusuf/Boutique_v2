# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.signup_screen import SignupScreenModel
from Controller.signup_screen import SignupScreenController
from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.splash_screen import SplashScreenModel
from Controller.splash_screen import SplashScreenController
from Model.email_verification_screen import EmailVerificationScreenModel
from Controller.email_verification_screen import EmailVerificationScreenController
from Model.profile_screen import ProfileScreenModel
from Controller.profile_screen import ProfileScreenController
from Model.orders_screen import OrdersScreenModel
from Controller.orders_screen import OrdersScreenController
from Model.address_screen import AddressScreenModel
from Controller.address_screen import AddressScreenController
from Model.detail_screen import DetailScreenModel
from Controller.detail_screen import DetailScreenController
from Model.cart_screen import CartScreenModel
from Controller.cart_screen import CartScreenController
from Model.checkout_screen import CheckoutScreenModel
from Controller.checkout_screen import CheckoutScreenController
from Model.search_screen import SearchScreenModel
from Controller.search_screen import SearchScreenController
from Model.scan_screen import ScanScreenModel
from Controller.scan_screen import ScanScreenController
from Model.orders_detail_screen import OrdersDetailScreenModel
from Controller.orders_detail_screen import OrdersDetailScreenController
from Model.order_status_screen import OrderStatusScreenModel
from Controller.order_status_screen import OrderStatusScreenController
from Model.categories_screen import CategoriesScreenModel
from Controller.categories_screen import CategoriesScreenController

screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
        'kv': 'View/LoginScreen/login_screen.kv'
    },
    "email verification screen": {
        "model": EmailVerificationScreenModel,
        "controller": EmailVerificationScreenController,
        'kv': 'View/EmailVerificationScreen/email_verification_screen.kv'
    },
    "signup screen": {
        "model": SignupScreenModel,
        "controller": SignupScreenController,
        'kv': 'View/SignupScreen/signup_screen.kv'
    },
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
        'kv': 'View/HomeScreen/home_screen.kv'
    },
    "splash screen": {
        "model": SplashScreenModel,
        "controller": SplashScreenController,
        'kv': 'View/SplashScreen/splash_screen.kv'
    },
    'profile screen': {
        'model': ProfileScreenModel,
        'controller': ProfileScreenController,
        'kv': 'View/ProfileScreen/profile_screen.kv'
    },
    'address screen': {
        'model': AddressScreenModel,
        'controller': AddressScreenController,
        'kv': 'View/AddressScreen/address_screen.kv'
    },
    'orders screen': {
        'model': OrdersScreenModel,
        'controller': OrdersScreenController,
        'kv': 'View/OrdersScreen/orders_screen.kv'
    },
    'detail screen': {
        'model': DetailScreenModel,
        'controller': DetailScreenController,
        'kv': 'View/DetailScreen/detail_screen.kv'
    },
    'checkout screen': {
        'model': CheckoutScreenModel,
        'controller': CheckoutScreenController,
        'kv': 'View/CheckoutScreen/checkout_screen.kv'
    },
    'orders detail screen': {
        'model': OrdersDetailScreenModel,
        'controller': OrdersDetailScreenController,
        'kv': 'View/OrdersDetailScreen/orders_detail_screen.kv'
    },
    'cart screen': {
        'model': CartScreenModel,
        'controller': CartScreenController,
        'kv': 'View/CartScreen/cart_screen.kv'
    },
    'search screen': {
        'model': SearchScreenModel,
        'controller': SearchScreenController,
        'kv': 'View/SearchScreen/search_screen.kv'
    },
    'scan screen': {
        'model': ScanScreenModel,
        'controller': ScanScreenController,
        'kv': 'View/ScanScreen/scan_screen.kv'
    },
    'order status screen': {
        'model': OrderStatusScreenModel,
        'controller': OrderStatusScreenController,
        'kv': 'View/OrderStatusScreen/order_status_screen.kv'
    },
    'categories screen': {
        'model': CategoriesScreenModel,
        'controller': CategoriesScreenController,
        'kv': 'View/CategoriesScreen/categories_screen.kv'
    },
}