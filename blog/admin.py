from django.contrib import admin

from .models import Author,Post,Tag,Comments

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author','tags','Date')
    list_display = ('title','author','Date')
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","text","post")

admin.site.register(Author)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Comments,CommentAdmin)