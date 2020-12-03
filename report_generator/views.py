from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import UploadFileForm, ResultsForm
from .utils import handle_uploaded_file, handle_results, send_email


# Create your views here.
def index(request):
    """View function for home page of site."""
    upload_form = UploadFileForm()
    results_form = ResultsForm(())
    return render(request, 'index.html', {
        'upload_form': upload_form,
        'results_form': results_form,
    })


def upload_file(request):

    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            csv_data = handle_uploaded_file(request.FILES['file'])
            thought_choices = [(index, row['thought'])
                               for (index, row) in enumerate(csv_data)]
            request.session['csv_data'] = csv_data
            results_form = ResultsForm(thought_choices)
            return render(request, 'index.html', {
                'upload_form': upload_form,
                'results_form': results_form
            })
        else:
            print(upload_form.errors)
    return HttpResponseRedirect(reverse('index'))


def generate_email(request):
    if request.method == 'POST':
        thought_choices = [(index, row['thought'])
                           for (index,
                                row) in enumerate(request.session['csv_data'])]
        results_form = ResultsForm(thought_choices, request.POST)
        if results_form.is_valid():
            results_data = handle_results(results_form)
            send_email(results_data)
            return render(request, 'email.html',
                          {'results_data': results_data})
        else:
            print(results_form.errors)
    return HttpResponseRedirect(reverse('index'))
