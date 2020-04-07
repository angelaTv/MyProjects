from django.urls import path
from product.views import ProductListView
from .views import *

app_name = 'ser'
urlpatterns = [
    path('', SearchProductListView.as_view(), name='query'),
    # path('<slug:slug>/', ProductDetailSlugView.as_view(), name='ar'),

]

# path('productLfun',product_listview),
# path('productDclass', ProductDetailView.as_view()),
# path('productDfun', product_detailview),
# path('productclass', ProductListView.as_view(), name='index'),
