from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings


class InvitationCode(models.Model):
    """Invitation code model"""
    code = models.CharField(blank=True, max_length=255, unique=True,
        verbose_name=_(u"Invitation code"))
    is_used = models.BooleanField(default=False,
        verbose_name=_(u"Is code used?"))
    user = models.ForeignKey(User, blank=True, null=True)
    used_date = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name=_(u"Used on"))

    def send_activation_email(self, site):
        """Send the activation mail"""
        from django.core.mail import EmailMultiAlternatives
        from django.template.loader import render_to_string

        ctx_dict = {'activation_key': self.activation_key,
                    'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
                    'site': site}
        subject = render_to_string('registration/activation_email_subject.txt',
                                   ctx_dict)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())

        message_text = render_to_string('registration/activation_email.txt', ctx_dict)
        message_html = render_to_string('registration/activation_email.html', ctx_dict)

        msg = EmailMultiAlternatives(subject, message_text, settings.DEFAULT_FROM_EMAIL, [self.user.email])
        msg.attach_alternative(message_html, "text/html")
        msg.send()
