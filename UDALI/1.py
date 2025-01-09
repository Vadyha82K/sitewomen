# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name='Изображение')
    content = models.TextField(blank=True, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin
from django.utils.safestring import mark_safe

# импорт from .models import Post

# здесь продолжайте программу
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
