from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from shop.models import Post, Tag, Post2, Post3,Post4, Post5,Post6, Post7,Post8, Post9,Post10,Post11, Post12

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_code','name','date','letter','tag','address')

class Post2Admin(admin.ModelAdmin):
    list_display = ('post_code2','name2','date2','letter2')


class Post3Admin(admin.ModelAdmin):
    list_display = ('post_code3', 'name3', 'date3', 'letter3','tag3')


class Post4Admin(admin.ModelAdmin):
    list_display = ('post_code4', 'name4', 'date4', 'letter4')


class Post5Admin(admin.ModelAdmin):
    list_display = ('post_code5', 'name5', 'date5', 'letter5')


class Post6Admin(admin.ModelAdmin):
    list_display = ('post_code6', 'name6', 'date6', 'letter6')


class Post7Admin(admin.ModelAdmin):
    list_display = ('post_code7', 'name7', 'date7', 'letter7')


class Post8Admin(admin.ModelAdmin):
    list_display = ('post_code8', 'name8', 'date8', 'letter8')

class Post9Admin(admin.ModelAdmin):
    list_display = ('post_code9', 'name9', 'date9', 'letter9')


class Post10Admin(admin.ModelAdmin):
    list_display = ('post_code10', 'name10', 'date10', 'letter10')


class Post11Admin(admin.ModelAdmin):
    list_display = ('post_code11', 'name11', 'date11', 'letter11')


class Post12Admin(admin.ModelAdmin):
    list_display = ('post_code12', 'name12', 'date12', 'letter12')

admin.site.register(Post, PostAdmin)
admin.site.register(Post2, Post2Admin)
admin.site.register(Post3, Post3Admin)
admin.site.register(Post4, Post4Admin)
admin.site.register(Post5, Post5Admin)
admin.site.register(Post6, Post6Admin)
admin.site.register(Post7, Post7Admin)
admin.site.register(Post8, Post8Admin)
admin.site.register(Post9, Post9Admin)
admin.site.register(Post10, Post10Admin)
admin.site.register(Post11, Post11Admin)
admin.site.register(Post12, Post12Admin)



class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Tag, TagAdmin)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']
