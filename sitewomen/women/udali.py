# --------- models.py ------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="Слаг"
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Контент")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


# --------- admin.py ------------------------
from django.contrib import admin

# импорт from .models import Post


# здесь продолжайте программу
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published", "info_post")
    list_display_links = ("title",)

    @admin.display(description="О заголовке")
    def info_post(self, post: Post):
        return f"Заголовок содержит {len(post.title.split())} слов"
