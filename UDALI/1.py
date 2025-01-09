# --------- models.py ------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="Слаг"
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    photo = models.ImageField(
        upload_to="post/%Y/%m/", blank=True, verbose_name="Изображение"
    )
    content = models.TextField(blank=True, verbose_name="Контент")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


# --------- admin.py ------------------------
from django.contrib import admin
from django.utils.safestring import mark_safe

# импорт from .models import Post


# здесь продолжайте программу
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ("title", "slug", "content", "photo", "is_published")
    list_display = ("title", "slug", "is_published", "post_photo")
    list_display_links = ("title",)
    list_editable = ("title", "slug", "content", "photo", "is_published")
    save_on_top = True

    @admin.display(description="Изображение")
    def post_photo(self, post: Post):
        return mark_safe(f"<img src='{post.photo.url}' width=50>")
