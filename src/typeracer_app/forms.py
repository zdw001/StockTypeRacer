from django import forms
from django.utils import html

class ContactForm(forms.Form):
    subject = forms.CharField(required=False, widget=forms.TextInput(
    	attrs={
    		'class': 'form-control',
    		'placeholder': 'Subject',
    	}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
        }))
    content = forms.CharField(required=True, widget=forms.TextInput(
    	attrs={
    		'class': 'form-control',
    		'placeholder': 'What would you like to say?',
    		'style': 'resize:none;'
    	}))

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].label = ''
        self.fields['contact_email'].label = ''
        self.fields['content'].label = ''
