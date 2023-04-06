from django.urls import path
from . import views
urlpatterns = [
        path("collection/<int:pk>",views.collection_detail,name="collection_detail"),
        path("collection/",views.collection,name="collection"),
        path("",views.home,name="home"),
        path("favourite",views.favourite_page,name="favourite"),
        path('save_carts/<int:input_value>/<int:product_id>/', views.save_carts, name="save_carts"),
        path("save_favourites/<int:pk>",views.save_favourites,name="save_favourites"),
        path("delete_favo/<int:pk>",views.delete_favo,name="delete_favo"),
        path("<slug:slug>",views.product_detail,name="product_detail"),

]
