from django.urls import path
from product.views import ProductListView
from .views import *

app_name = 'cart'
urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name='update'),
    path('checkout/',checkout_home, name='checkout'),
    path('checkout/success/',checkout_doneView, name='success'),
]

# path('productLfun',product_listview),
# path('productDclass', ProductDetailView.as_view()),
# path('productDfun', product_detailview),
# path('productclass', ProductListView.as_view(), name='index'),
