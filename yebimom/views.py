# -*- coding: utf-8 -*-

from django.shortcuts import render

# Forms
from yebimom.forms import ContactForm

# Tasks
from yebimom.tasks import send_sms
from yebimom.tasks import send_contact_email


def home(request):
    return render(request, "home.html", {})


def service(request):
    """
    이용약관
    """
    return render(request, "rules/service.html", {})


def privacy(request):
    """
    개인정보 취급방침
    """
    return render(request, "rules/privacy.html", {})


def disclaimer(request):
    """
    책임의 한계와 법적고지
    """
    return render(request, "rules/disclaimer.html", {})


def search_policy(request):
    """
    검색결과 수집에 대한 정책
    """
    return render(request, "rules/search_policy.html", {})


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        title = request.POST.get('title')
        content = request.POST.get('content')

        send_sms.delay(
            {
                'dest_phone': phone,
                'dest_name': phone,
                'msg_body': "[예비맘닷컴] 1:1 문의가 접수되었습니다. 빠르게 연락드리겠습니다. 감사합니다."
            }
        )

        send_contact_email.delay(email, title, content, phone)
    else:
        pass

    return render(request, "contact.html", {
        'form': form
    })
