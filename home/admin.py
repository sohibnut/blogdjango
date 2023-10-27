from django.contrib import admin
from .models import Banner, Comment, Aboutus, Service, Contact
# Register your models here.

admin.site.register(Banner)
admin.site.register(Aboutus)

@admin.register(Comment)
class NewComment(admin.ModelAdmin):
    list_display = ["id", "name", "email", "time"]
    readonly_fields = ["name", "email"]

admin.site.register(Service)
admin.site.register(Contact)
