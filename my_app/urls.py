
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_seller, name='register_seller'),
    # path('login/', views.login_seller, name='login_seller'),
    path('logout/', views.logout_view, name='logout'),
    # path('orders/', views.orders, name='orders'),
    path('buy/', views.buy, name='buy'),
    path('buy_product/', views.buy_product, name='buy_product'),
    path('sell/', views.sell, name='sell'),
    path('seller_product_details/', views.seller_product_details, name='seller_product_details'),
    path('order-login/', views.order_login, name='order_login'),
    path('order-register/', views.order_register, name='order_register'),
    path('buy/<int:product_id>/', views.buy, name='buy_product'),
    path('thank_you/<int:order_id>/', views.thank_you, name='thank_you'),
    path('order-product-details/', views.order_product_details, name='order_product_details'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('buy_product/<int:product_id>/', views.buy_product, name='buy_product'),
    path('sold-product-details/', views.sold_product_details, name='sold_product_details'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('buy_product/<int:product_id>/', views.buy_product, name='buy_product'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('api/product-details/<int:product_id>/',views.buy_view, name='product-details'),
    path('products/', views.product_list, name='product-list'),  # Ensure 'product-list' is used here
    path('products/<int:id>/', views.product_detail, name='product-detail'),  # URL for product detail
  path('buy/<int:product_id>/', views.buy_product, name='buy-product'),

  # URL for buying a product
   path('thank-you/<int:order_id>/', views.thank_you, name='thank-you'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

