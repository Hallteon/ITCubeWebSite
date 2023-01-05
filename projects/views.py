from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView
from slugify import slugify

from articles.models import Category, Tag
from notifications.models import Notice
from projects.forms import AddProjectForm
from projects.models import Project
from utils.utils import DataMixin


class UserProjects(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/user_projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(author=self.request.user).order_by('-create_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Проекты пользователя'

        return context


class AddProject(LoginRequiredMixin, CreateView):
    form_class = AddProjectForm
    template_name = 'projects/add_project.html'

    def get_success_url(self):
        return reverse('project', kwargs={'project_slug': self.obj.slug})

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.slug = slugify(self.obj.name)
        self.obj.save()

        self.obj.members.add(self.request.user)
        self.obj.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить проект'

        return context


class ShowProjects(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(public=True).order_by('-create_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Проекты'
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()

        return context


class ShowProject(LoginRequiredMixin, DataMixin, DetailView):
    model = Project
    template_name = 'projects/project.html'
    slug_url_kwarg = 'project_slug'
    context_object_name = 'project'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['project']

        return context