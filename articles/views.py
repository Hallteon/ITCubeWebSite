from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin, DeleteView, UpdateView

from articles.forms import AddArticleForm, AddCommentForm, UpdateArticleForm
from articles.models import Article, Comment
from tags.models import Tag
from utils.utils import DataMixin


class DeleteComment(DeleteView):
    model = Comment
    pk_url_kwarg = 'comment_id'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()

        if self.obj.author.pk == self.request.user.pk or self.request.user.is_superuser():
            self.success_url = self.get_success_url()
            self.obj.delete()

            return HttpResponseRedirect(self.success_url)

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'article_id': self.get_object().article.pk})


class ShowArticles(DataMixin, ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by('-create_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()

        c_def = self.get_user_context(title='Статьи')

        return dict(list(context.items()) + list(c_def.items()))


class ShowArticle(LoginRequiredMixin, FormMixin, DataMixin, DetailView):
    model = Article
    template_name = 'articles/article.html'
    pk_url_kwarg = 'article_id'
    context_object_name = 'article'
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'article_id': self.get_object().pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.article = self.get_object()
        obj.save()

        messages.success(self.request, 'Вы добавили комментарий.')

        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.user not in self.get_object().views_count.all():
            self.get_object().views_count.add(self.request.user)

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['article']))

        return dict(list(context.items()) + list(c_def.items()))


class AddArticle(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddArticleForm
    template_name = 'articles/add_article.html'
    success_url = reverse_lazy('articles')

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создание статьи')
        return dict(list(context.items()) + list(c_def.items()))


class UpdateArticle(UpdateView):
    model = Article
    template_name = 'articles/update_article.html'
    form_class = UpdateArticleForm
    pk_url_kwarg = 'article_id'

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'article_id': self.kwargs['article_id']})

    def form_valid(self, form):
        if self.get_object().author.pk == self.request.user.pk or self.request.user.is_superuser():
            form.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование статьи'

        return context


class DeleteArticle(DeleteView):
    model = Article
    pk_url_kwarg = 'article_id'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()

        if self.obj.author.pk == self.request.user.pk or self.request.user.is_superuser():
            self.success_url = self.get_success_url()
            self.obj.delete()

            return HttpResponseRedirect(self.success_url)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'profile_slug': self.get_object().author.username})
