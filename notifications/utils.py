from notifications.models import Notice


class NoticeMixin:

    def send_notice(self, user_to, text):
        Notice.objects.create(user_to=user_to, text=text)