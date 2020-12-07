import csv
import os
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from pathlib import Path
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import date


def handle_uploaded_file(f):
    decoded_file = f.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    data = []
    prompt = ""
    for row in reader:
        if prompt == "":
            prompt = row['\ufeffExchange question']
        data.append({
            'thought': row['Thought (original)'],
            "star": row['Star score - overall'],
            "rank": row['Rank - overall']
        })
    return (data, prompt)


def handle_results(form):
    categories = ["thoughts4", "thoughts3", "thoughts2", "thoughts1", "thoughts0"]
    thoughts = []
    for category in categories:
        selected = form.cleaned_data[category]
        choices = dict(form.fields[category].choices)
        for item in selected:
            thoughts.append(choices[int(item)])
    data = form.cleaned_data
    data['thoughts'] = thoughts
    return data


def send_email(results_data):
    today = date.today().strftime("%m/%d/%y")
    subject = f'{today} ThoughtExchange Report | Summary & Response'
    sender = 'cs96.test@gmail.com'
    recipient = results_data['recipient']
    msg_html = render_to_string('email.html', {'results_data': results_data})
    msg_plain = strip_tags(msg_html)

    email = EmailMultiAlternatives(
        subject=subject,
        body=msg_plain,
        from_email=sender,
        to=recipient if isinstance(recipient, list) else [recipient])

    image_path = 'static/i/logo.png'
    if all([msg_html, image_path]):
        email.attach_alternative(msg_html, "text/html")
        email.mixed_subtype = 'related'
        with open(image_path, mode='rb') as f:
            image = MIMEImage(f.read())
            f.close()
            image.add_header('Content-ID', "<logo>")
            email.attach(image)

    email.send()
