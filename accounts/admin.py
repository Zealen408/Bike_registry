from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



from .models import *
from .forms import *

# admin site classes

class myUserAdmin(BaseUserAdmin):
    # forms
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # List display
    list_display = ('email', 'get_full_name', 'phone')
    search_fields = ('email', 'get_full_name', 'state')
    ordering = ['email']
    filter_horizontal = []
    list_filter = []

    # Detail display
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone')}),
        (None, {'fields': ('first_name', 'last_name')}),
        ('admin', {'classes': ('collapse',), 'fields': (('active', 'law_enforcement', 'staff'))}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )



# Register your models here.

# admin.site.register(state)
admin.site.register(myUser, myUserAdmin)
admin.site.unregister(Group)