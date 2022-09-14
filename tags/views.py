from django.views.generic import ListView

from articles.models import Article
from projects.models import Project
from tags.models import Tag
from utils.utils import DataMixin


class ShowTagArticles(DataMixin, ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    allow_empty = True

    def get_queryset(self):
        return Article.objects.filter(tags__slug=self.kwargs['tag_slug'], is_published=True).order_by('-create_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['tag'] = Tag.objects.get(slug=self.kwargs['tag_slug'])

        selected_tag = Tag.objects.get(slug=self.kwargs['tag_slug'])
        c_def = self.get_user_context(title=str(selected_tag.name), selected_tag=selected_tag.pk)

        return dict(list(context.items()) + list(c_def.items()))


class ShowTagProjects(DataMixin, ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    allow_empty = True

    def get_queryset(self):
        return Project.objects.filter(tags__slug=self.kwargs['tag_slug'], public=True).order_by('-create_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['tag'] = Tag.objects.get(slug=self.kwargs['tag_slug'])

        selected_tag = Tag.objects.get(slug=self.kwargs['tag_slug'])
        c_def = self.get_user_context(title=str(selected_tag.name), selected_tag=selected_tag.pk)

        return dict(list(context.items()) + list(c_def.items()))