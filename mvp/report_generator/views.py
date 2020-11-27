from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import UploadFileForm, ResultsForm
from .utils import handle_uploaded_file, handle_results


# Create your views here.
def index(request):
    """View function for home page of site."""
    upload_form = UploadFileForm()
    results_form = ResultsForm()
    return render(request, 'index.html', {
        'upload_form': upload_form,
        'results_form': results_form,
        'data': []
    })


def upload_file(request):

    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            data = handle_uploaded_file(request.FILES['file'])
            results_form = ResultsForm()
            return render(
                request, 'index.html', {
                    'upload_form': upload_form,
                    'results_form': results_form,
                    'data': data
                })
        else:
            print(upload_form.errors)
    return HttpResponseRedirect(reverse('index'))


def generate_email(request):
    if request.method == 'POST':
        results_form = ResultsForm(request.POST)
        if results_form.is_valid():
            results_data = handle_results(results_form.cleaned_data)
            msg_plain = render_to_string('email.txt',
                                         {'results_data': results_data})
            msg_html = render_to_string('email.html',
                                        {'results_data': results_data})

            send_mail('Summary Report',
                      msg_plain,
                      'cs96.test@gmail.com', [results_data['recipient']],
                      html_message=msg_html)

            return HttpResponse('success')
        else:
            print(results_form.errors)
    return HttpResponseRedirect(reverse('index'))