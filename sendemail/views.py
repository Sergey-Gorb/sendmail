# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template import Engine, Context
import smtplib
from PIL import Image
from mailer.celery import app


def render_template(template, context):
    engine = Engine.get_default()
    tmpl = engine.get_template(template)
    return tmpl.render(Context(context))


@app.task(bind=True, default_retry_delay=10 * 60)
def send_mail_task(self, recipients, subject, template, context):
    
    message = render_template('{0!r}'.format(template) + '.txt', context)
    html_message = render_template('{0!r}'.format(template) + '.html', context)
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipients,
            fail_silently=False,
            html_message=html_message
        )
    except smtplib.SMTPException as ex:
        self.retry(exc=ex)


def index(request):
    return HttpResponse("Hello, world. You're at index.")


def image_load(request):
    print("\nImage Loaded\n")
    red = Image.new('RGB', (1, 1))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")
    return response
