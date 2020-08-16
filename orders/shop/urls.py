from django.urls import path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CategoryView, ShopView, ProductInfoView, BasketView, OrderView, LoginAccount, ContactView, \
    AccountDetails, ConfirmAccount, RegisterAccount, PartnerOrders, PartnerState, PartnerUpdate

app_name = 'shop'

router = routers.SimpleRouter()
router.register(r'shops', ShopView)
router.register(r'categories', CategoryView)
router.register(r'products', ProductInfoView, basename='products')

urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
    path('', include(router.urls)),
]

urlpatterns += router.urls
