from django.urls import path
from .views import home_shop, detail_shop, create_shop, delete_shop, update_shop

urlpatterns = [
    path('', home_shop, name='home'),
    path('detail-shop/<int:id>/', detail_shop, name='detail-shop'),
    path('create-shop/', create_shop, name='create-shop'),
    path('delete-shop/<int:id>/', delete_shop, name='delete-shop'),
    path('update-shop/<int:id>/', update_shop, name='update-shop')
]
