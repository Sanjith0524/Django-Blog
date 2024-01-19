from django.contrib import admin

from .models import Author,Post,Tag

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author','tags','Date')
    list_display = ('title','author','Date')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Author)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)