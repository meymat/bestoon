from django.contrib import admin
from.models import Expense 




class ExpenseAdmin(admin.ModelAdmin):
    list_display=("user","date","amount","text") 
    list_filter=("user","date")
    list_editable=("text",)
    list_display_links=("date",)
    search_fields=("amount",)

admin.site.register(Expense,ExpenseAdmin)