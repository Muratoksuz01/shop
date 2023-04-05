from django.contrib import admin
from . models import Product ,Catagorys,Favourites,Carts
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","slug")#admin sayfasına gelince başlıgı  ve diğerlerini burakadkileri sadece direkt görmeni saglar
    readonly_fields=["slug"]#bloga tıkladıgında slug ları değiştiremessin artık  sadece görmen için 


admin.site.register(Product,ProductAdmin)
admin.site.register(Catagorys)
admin.site.register(Favourites)
admin.site.register(Carts)


