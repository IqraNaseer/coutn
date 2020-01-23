from django.contrib import admin
from .models import product
from .models import Contact
from .models import Orders
from .models import Booking
from .models import select
from .models import measurement
# Register your models here.

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(Booking)
admin.site.register(select)
admin.site.register(measurement)