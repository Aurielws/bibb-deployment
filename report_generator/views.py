from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
<<<<<<< HEAD
from .forms import UploadFileForm, ResultsForm, EmailForm
from .utils import handle_uploaded_file, handle_results, send_email
from django.template.loader import render_to_string

=======
from django.utils.html import strip_tags
from .forms import UploadFileForm, ResultsForm
from .utils import handle_uploaded_file, handle_results
from datetime import date
>>>>>>> 24a10f37c199e149676d6ec48fbd1b87be68bdc3

# Create your views here.
def index(request):
    """View function for home page of site."""
    request.session.flush()
    upload_form = UploadFileForm()
    return render(request, 'upload.html', {
        'upload_form': upload_form,
    })


def upload_file(request):

    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            csv_data, prompt = handle_uploaded_file(request.FILES['file'])
            thought_choices = [(index, row['thought'])
                               for (index, row) in enumerate(csv_data)]
            request.session['csv_data'] = csv_data
            request.session['prompt'] = prompt
            results_form = ResultsForm(thought_choices)
            return render(request, 'review.html', {
                'results_form': results_form,
                'prompt': prompt
            })
        else:
            print(upload_form.errors)
    return HttpResponseRedirect(reverse('index'))


def preview(request):
    if request.method == 'POST':
        thought_choices = [(index, row['thought'])
                           for (index,
                                row) in enumerate(request.session['csv_data'])]
        results_form = ResultsForm(thought_choices, request.POST)
        if results_form.is_valid():
            results_data = handle_results(results_form)
<<<<<<< HEAD
            results_data['prompt'] = request.session['prompt']
            results_data['image_path'] = "cid:logo"
            website_msg_html = render_to_string('web_email.html',
                                                {'results_data': results_data})
            send_email(results_data)
            return render(request, 'success.html',
                          {'msg_html': website_msg_html})
=======
            question = request.session['csv_data'][0]['question']
            msg_html = render_to_string('email.html',
                                        {'results_data': results_data,
                                        'question': question})
            msg_plain = strip_tags(msg_html)

            today = date.today()

            send_mail(today.strftime("%m/%d/%y") + ' ' + 'ThoughtExchange Report | Summary & Response',
                      msg_plain,
                      'cs96.test@gmail.com', [results_data['recipient']],
                      html_message=msg_html)

            return render(request, 'success.html', {'msg_html': msg_html})
>>>>>>> 24a10f37c199e149676d6ec48fbd1b87be68bdc3
        else:
            print(results_form.errors)
    return HttpResponseRedirect(reverse('index'))
