from django.views.generic import ListView

from articles.models import Article
from categories.models import Category
from projects.models import Project
from tags.models import Tag
from utils.utils import DataMixin


class ShowCategoryArticles(DataMixin, ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    allow_empty = True

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True).order_by('-create_time').select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.filter(category__slug=self.kwargs['category_slug'])
        context['category'] = Category.objects.get(slug=self.kwargs['category_slug'])

        selected_cat = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title=str(selected_cat.name), selected_cat=selected_cat.pk)

        return dict(list(context.items()) + list(c_def.items()))


class ShowCategoryProjects(DataMixin, ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    allow_empty = True

    def get_queryset(self):
        return Project.objects.filter(category__slug=self.kwargs['category_slug'], public=True).order_by('-create_time').select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.filter(category__slug=self.kwargs['category_slug'])
        context['category'] = Category.objects.get(slug=self.kwargs['category_slug'])

        selected_cat = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title=str(selected_cat.name), selected_cat=selected_cat.pk)

        return dict(list(context.items()) + list(c_def.items()))
