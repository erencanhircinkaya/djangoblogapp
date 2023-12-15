from django.contrib import admin
from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"] #title author ve created_date gözükmesi
    list_display_links = ["title","created_date"] #title ve created_date link koyma ve içeriği görme
    search_fields = ["title"] #title'a göre arama yapma
    list_filter = ["created_date"] #tarihe göre içeriği bulma
    

    class Meta:
        model = Article
