from django.urls import path
from . import views
urlpatterns = [
        path("",views.home,name="home"),
        path("favourite",views.favourite_page,name="favourite"),
        path("save_favourites/<int:pk>",views.save_favourites,name="save_favourites"),
        path("save_carts/<int:pk>",views.save_carts,name="save_carts"),
        path("delete_favo/<int:pk>",views.delete_favo,name="delete_favo"),
        path("<slug:slug>",views.product_detail,name="product_detail"),
       







]
