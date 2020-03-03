from django.contrib import admin
from .models import Category
from .models import Catalog
from .models import Inventory
from .models import Producer

# Register your models here.
admin.site.register(Category)
admin.site.register(Catalog)
admin.site.register(Inventory)
admin.site.register(Producer)
