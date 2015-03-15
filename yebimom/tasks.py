# -*- coding: utf-8 -*-

from __future__ import absolute_import
from celery import shared_task

import requests

# Email
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context

# SMS
from yebimom.settings.partials.application import API_STORE_KEY
from yebimom.settings.partials.application import API_STORE_BASE_URL
from yebimom.settings.partials.application import SMS_SEND_PHONE
from yebimom.settings.partials.application import SMS_SEND_NAME
from yebimom.settings.partials.application import SMS_SUBJECT


@shared_task
def send_contact_email(email, title, content, phone):
    email_template = get_template('email/contact.html')
    email_context = Context({
        'content': content
    })

    # send email to customer
    send_mail(
        "[예비맘닷컴] 1:1 문의가 등록되었습니다",
        email_template.render(email_context),
        "예비맘 <contact@yebimom.com>",
        [email],
        fail_silently=False,
    )

    email_template = get_template('email/admin/contact.html')
    email_context = Context({
        'title': title,
        'content': content,
        'email': email,
        'phone': phone,
    })

    # send email to admin
    send_mail(
        "[1:1 문의] " + title.encode('utf-8'),
        email_template.render(email_context),
        "예비맘 <contact@yebimom.com>",
        ["contact@yebimom.com"],
        fail_silently=False,
    )


# SMS
@shared_task
def send_sms(data):
    """
    In case of sending email, each email sending process has
    independent "template" and "context".
    so, it is hard to write it in a celery task module.

    but, in case of sending sms, each sms has very simple and common process.
    so i have wrote this module as "send_sms" working in background with Celery, Redis

    # Usage
    send_sms.delay(data)

    data should have 3 arguments.
    data = {
        'dest_phone': "...",
        'dest_name': "...",
        'msg_body': "...",
    }
    """

    headers = {
        'x-waple-authorization': API_STORE_KEY
    }

    if 'send_phone' not in data.keys():
        data['send_phone'] = SMS_SEND_PHONE
    if 'send_name' not in data.keys():
        data['send_name'] = SMS_SEND_NAME
    if 'subject' not in data.keys():
        data['subject'] = SMS_SUBJECT

    request = requests.post(
        API_STORE_BASE_URL, data=data, headers=headers
    )
