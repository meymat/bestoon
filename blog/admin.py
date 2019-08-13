from django.contrib import admin
from.models import Expense ,Income , Token




class ExpenseAdmin(admin.ModelAdmin):
    list_display=("user","date","amount","text") 
    list_filter=("user","date")
    list_editable=("text",)
    list_display_links=("date",)
    search_fields=("amount",)

admin.site.register(Expense,ExpenseAdmin)





class IncomeAdmin(admin.ModelAdmin):
    list_display=("user","date","amount","text") 
    list_filter=("user","date")
    list_editable=("text",)
    list_display_links=("date",)
    search_fields=("amount",)


admin.site.register(Income,IncomeAdmin)



class TokenAdmin(admin.ModelAdmin):
    list_display=("user","token") 
    list_filter=("user","token")
#     
    list_display_links=("token",)
    search_fields=("user",)

admin.site.register(Token,TokenAdmin)