from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from notifications.forms import SendProjectApplicationForm
from notifications.models import Notice, ProjectApplication
from notifications.utils import NoticeMixin
from projects.models import Project


class ShowNotices(LoginRequiredMixin, ListView):
    model = Notice
    template_name = 'notifications/notifications.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notice.objects.filter(user_to=self.request.user).order_by('-create_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Уведомления'

        return context


class ConfirmNotice(DeleteView):
    model = Notice
    pk_url_kwarg = 'notice_id'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()

        if self.obj.to_user.pk == self.request.user.pk or self.request.user.is_superuser():
            self.success_url = self.get_success_url()

            self.obj.delete()

            return HttpResponseRedirect(self.success_url)

    def get_success_url(self):
        return reverse_lazy('notifications')


class SendProjectApplication(LoginRequiredMixin, NoticeMixin, CreateView):
    form_class = SendProjectApplicationForm
    template_name = 'projects/send_project_application.html'
    success_url = reverse_lazy('projects')
    slug_url_kwarg = 'project_slug'

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user
        self.obj.project = Project.objects.get(slug=self.kwargs['project_slug'])
        self.obj.save()

        self.send_notice(user_to=self.obj.project.author, text=f'На ваш проект "{self.obj.project.name}" была подана заявка '
                                   f'от пользователя {self.request.user}.')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отправить завку на проект'

        return context


class ConfirmProjectApplication(NoticeMixin, DeleteView):
    model = ProjectApplication
    pk_url_kwarg = 'application_id'

    def form_valid(self, form):
        Project.objects.get(slug=self.get_object().project.slug).members.add(self.get_object().user)
        Project.objects.get(slug=self.get_object().project.slug).save()

        self.send_notice(user_to=self.get_object().user,
                         text=f'Ваша заявка на проект "{self.get_object().project.name}" была принята!')

        return super().form_valid(form)

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()

        if self.obj.project.author.pk == self.request.user.pk or self.request.user.is_superuser():
            self.success_url = self.get_success_url()

            self.obj.delete()

            return HttpResponseRedirect(self.success_url)

    def get_success_url(self):
        return reverse_lazy('project', kwargs={'project_slug': self.get_object().project.slug})


class RejectProjectApplication(NoticeMixin, DeleteView):
    model = ProjectApplication
    pk_url_kwarg = 'application_id'

    def form_valid(self, form):
        self.send_notice(user_to=self.get_object().user,
                         text=f'Ваша заявка на проект "{self.get_object().project.name}" была отколнена!')

        return super().form_valid(form)

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()

        if self.obj.project.author.pk == self.request.user.pk or self.request.user.is_superuser():
            self.success_url = self.get_success_url()

            self.obj.delete()

            return HttpResponseRedirect(self.success_url)

    def get_success_url(self):
        return reverse_lazy('user_projects')