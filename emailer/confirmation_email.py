from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token


class EmailConfirmation:

    def email_user(request, user, mail_subject, template):

        current_site = get_current_site(request)
        message = render_to_string(template, {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })
        to_email = user.email
        email = EmailMessage(mail_subject, message, to=[to_email])
        return email.send()

