from django.contrib import admin
from .models import Transaction

class AuthorAdmin(admin.ModelAdmin):
    model = Transaction
    list_display  = ['text','amount','id']

# Register your models here.
admin.site.register(Transaction,AuthorAdmin) 