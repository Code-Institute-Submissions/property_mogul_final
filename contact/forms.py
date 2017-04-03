from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your e-mail address here'}))
    cc_myself = forms.BooleanField(required=False)
