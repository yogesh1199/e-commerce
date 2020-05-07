from django.contrib import admin

# Register your models here.
from . models import product,Contact,orders,order_update
admin.site.register(product)


admin.site.register(Contact)

admin.site.register(orders)

admin.site.register(order_update)