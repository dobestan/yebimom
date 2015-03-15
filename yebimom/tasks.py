# -*- coding: utf-8 -*-

from __future__ import absolute_import
from celery import shared_task


# Email
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context


@shared_task
def send_contact_email(email, title, content):
    email_template = get_template('email/contact.html')
    email_context = Context({
        'content': content
    })

    # send email to customer
    send_mail(
        "[예비맘닷컴] 1:1 문의가 등록되었습니다.",
        email_template.render(email_context),
        "예비맘 <contact@yebimom.com>",
        [email],
        fail_silently=False,
    )

    # send email to admin
    send_mail(
        "[예비맘닷컴] 1:1 문의가 등록되었습니다. - " + title.encode('utf-8'),
        content,
        "예비맘 <contact@yebimom.com>",
        ["contact@yebimom.com"],
        fail_silently=False,
    )
