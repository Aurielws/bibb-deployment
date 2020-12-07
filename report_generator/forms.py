from django import forms
from django.forms import ModelForm
from crispy_forms.bootstrap import Tab, TabHolder, Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ResultsForm(forms.Form):
    def __init__(self, thought_choices, *args, **kwargs):
        super(ResultsForm, self).__init__(*args, **kwargs)
        thought_choices_sorted = {"0":[], "1":[], "2":[], "3":[], "4":[]}
        for row in thought_choices:
            # need to check what happens if a thought has no star score (NaN??)
            category = str(int(float(row[2])))
            thought_choices_sorted[category].append((row[0], row[1]))

        self.fields['thoughts4'].choices = thought_choices_sorted["4"]
        self.fields['thoughts3'].choices = thought_choices_sorted["3"]
        self.fields['thoughts2'].choices = thought_choices_sorted["2"]
        self.fields['thoughts1'].choices = thought_choices_sorted["1"]
        self.fields['thoughts0'].choices = thought_choices_sorted["0"]

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            TabHolder(
                Tab('4-5 Stars', 'thoughts4'),
                Tab('3-4 Stars', 'thoughts3'),
                Tab('2-3 Stars', 'thoughts2'),
                Tab('1-2 Stars', 'thoughts1'),
                Tab('0-1 Stars', 'thoughts0')
            )
        )


    thoughts4 = forms.MultipleChoiceField(choices=(),
                                             widget=forms.CheckboxSelectMultiple(),
                                             required=False)
    thoughts3 = forms.MultipleChoiceField(choices=(),
                                             widget=forms.CheckboxSelectMultiple(),
                                             required=False)
    thoughts2 = forms.MultipleChoiceField(choices=(),
                                             widget=forms.CheckboxSelectMultiple(),
                                             required=False)
    thoughts1 = forms.MultipleChoiceField(choices=(),
                                             widget=forms.CheckboxSelectMultiple(),
                                             required=False)
    thoughts0 = forms.MultipleChoiceField(choices=(),
                                             widget=forms.CheckboxSelectMultiple(),
                                             required=False)

    summary = forms.CharField(label='Write your summary here.',
                              max_length=1000,
                              widget=forms.Textarea)
    action = forms.CharField(label="What are you going to do?",
                             max_length=1000,
                             widget=forms.Textarea)
    recipient = forms.EmailField(label="Email recipient here:")


class EmailForm(forms.Form):
    recipient = forms.EmailField(label="Email recipient here:")
