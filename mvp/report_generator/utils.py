import csv
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives


def handle_uploaded_file(f):
    decoded_file = f.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    data = []
    for row in reader:
        data.append({
            'prompt': row['Exchange question'],
            'thought': row['Thought (original)'],
            "star": row['Star score - overall'],
            "rank": row['Rank - overall']
        })
    return data


def handle_results(form):
    selected = form.cleaned_data['thoughts']
    choices = dict(form.fields['thoughts'].choices)
    thoughts = [choices[int(item)] for item in selected]
    data = form.cleaned_data
    data['thoughts'] = thoughts
    return data


def send_email(subject, text_content, html_content, sender, recipient,
               image_path, image_name):
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=sender,
        to=recipient if isinstance(recipient, list) else [recipient])
    if all([html_content, image_path, image_name]):
        email.attach_alternative(html_content, "text/html")
        email.content_subtype = 'html'  # set the primary content to be text/html
        email.mixed_subtype = 'related'  # it is an important part that ensures embedding of an image
        with open(image_path, mode='rb') as f:
            image = MIMEImage(f.read())
            email.attach(image)
            image.add_header('Content-ID', f"<{image_name}>")
    email.send()
