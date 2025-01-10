# --------- models.py ------------------------
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


# --------- views.py ------------------------
from django.views.generic import DetailView

# from django.shortcuts import get_object_or_404
# from .models import Post


# здесь объявляйте класс представления
class PostDetail(DetailView):
    template_name = "post/detail_post.html"
    context_object_name = "post"
    slug_url_kwarg = "post_slug"

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.slug_url_kwarg, is_published=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Заголовок поста"
        context["cat_selected"] = 0
        return context
