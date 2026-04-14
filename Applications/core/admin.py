from django.contrib import admin
from .models import Profile, Organization, GeneratedFood, Publication, Items_Publication, Schedules, Delivery, Qualification

# Register your models here.
admin.site.register(Profile)
admin.site.register(Organization)
admin.site.register(GeneratedFood)
admin.site.register(Publication)
admin.site.register(Items_Publication)
admin.site.register(Schedules)
admin.site.register(Delivery)
admin.site.register(Qualification)