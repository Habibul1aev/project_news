from django.contrib import admin
from .models import News, Category
from django.utils.safestring import mark_safe

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'update_at', 'is_publish', 'bigPhoto')
    list_display_links = ('id', 'title') 
    search_fields = ('id', 'title')
    readonly_fields = ['created_at','innerPhoto']

    def bigPhoto(self, news=News):
        return mark_safe(f'<img src="{news.photo.url}" width="150px">')
    
    def innerPhoto(self, news=News):
        return mark_safe(f'<img src="{news.photo.url}" width="200px">')

        

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title') 
    search_fields = ('title',)



admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
