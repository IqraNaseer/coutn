from django.contrib import admin

# Register your models here.

from .models import product
from .models import Contact
from .models import Orders
from .models import bookrequest
from .models import loginform



admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(bookrequest)
admin.site.register(loginform)

