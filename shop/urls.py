from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path('search/', views.search_user, name='search-user'),
    path('about/', views.about, name='AboutUs'),

]
