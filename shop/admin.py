from django.contrib import admin
from shop.models import Post, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_code','name','date','letter')

admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Tag, TagAdmin)
