from django.contrib import admin
from .models import posts
from .models import Contact
from .models import menutab


# Register your models here.

class postView(admin.ModelAdmin):
    list_display = [
        'post_title',
        'post_time',
        'post_auther'
    ]


class contactView(admin.ModelAdmin):
    list_display = [
        'name',
        'contacttime',
        'email',
        'category',
        'subject'
    ]

class menutabView(admin.ModelAdmin):
    list_display = [
        'menu_title',
        'menu_adres'
    ]


admin.site.register(Contact, contactView)
admin.site.register(posts, postView)
admin.site.register(menutab, menutabView)
